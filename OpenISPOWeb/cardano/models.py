# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdaPots(models.Model):
    id = models.BigAutoField(primary_key=True)
    slot_no = models.IntegerField()
    epoch_no = models.IntegerField()
    treasury = models.DecimalField(max_digits=20, decimal_places=0)
    reserves = models.DecimalField(max_digits=20, decimal_places=0)
    rewards = models.DecimalField(max_digits=20, decimal_places=0)
    utxo = models.DecimalField(max_digits=20, decimal_places=0)
    deposits = models.DecimalField(max_digits=20, decimal_places=0)
    fees = models.DecimalField(max_digits=20, decimal_places=0)
    block = models.OneToOneField('Block', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ada_pots'


class AdminUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=-1)
    password = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'admin_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Block(models.Model):
    id = models.BigAutoField(primary_key=True)
    hash = models.BinaryField(unique=True)
    epoch_no = models.IntegerField(blank=True, null=True)
    slot_no = models.IntegerField(blank=True, null=True)
    epoch_slot_no = models.IntegerField(blank=True, null=True)
    block_no = models.IntegerField(blank=True, null=True)
    previous = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    slot_leader = models.ForeignKey('SlotLeader', models.DO_NOTHING)
    size = models.IntegerField()
    time = models.DateTimeField()
    tx_count = models.BigIntegerField()
    proto_major = models.IntegerField()
    proto_minor = models.IntegerField()
    vrf_key = models.CharField(max_length=-1, blank=True, null=True)
    op_cert = models.BinaryField(blank=True, null=True)
    op_cert_counter = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block'


class CollateralTxIn(models.Model):
    id = models.BigAutoField(primary_key=True)
    tx_in = models.ForeignKey('Tx', models.DO_NOTHING)
    tx_out = models.ForeignKey('Tx', models.DO_NOTHING)
    tx_out_index = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'collateral_tx_in'
        unique_together = (('tx_in', 'tx_out', 'tx_out_index'),)


class CostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    costs = models.JSONField(unique=True)
    block = models.ForeignKey(Block, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cost_model'


class Datum(models.Model):
    id = models.BigAutoField(primary_key=True)
    hash = models.BinaryField(unique=True)
    tx = models.ForeignKey('Tx', models.DO_NOTHING)
    value = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datum'


class Delegation(models.Model):
    id = models.BigAutoField(primary_key=True)
    addr = models.ForeignKey('StakeAddress', models.DO_NOTHING)
    cert_index = models.IntegerField()
    pool_hash = models.ForeignKey('PoolHash', models.DO_NOTHING)
    active_epoch_no = models.BigIntegerField()
    tx = models.ForeignKey('Tx', models.DO_NOTHING)
    slot_no = models.IntegerField()
    redeemer = models.ForeignKey('Redeemer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delegation'
        unique_together = (('addr', 'pool_hash', 'tx'),)


class DelistedPool(models.Model):
    id = models.BigAutoField(primary_key=True)
    hash_raw = models.BinaryField(unique=True)

    class Meta:
        managed = False
        db_table = 'delisted_pool'


class Epoch(models.Model):
    id = models.BigAutoField(primary_key=True)
    out_sum = models.DecimalField(max_digits=39, decimal_places=0)
    fees = models.DecimalField(max_digits=20, decimal_places=0)
    tx_count = models.IntegerField()
    blk_count = models.IntegerField()
    no = models.IntegerField(unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'epoch'


class EpochParam(models.Model):
    id = models.BigAutoField(primary_key=True)
    epoch_no = models.IntegerField()
    min_fee_a = models.IntegerField()
    min_fee_b = models.IntegerField()
    max_block_size = models.IntegerField()
    max_tx_size = models.IntegerField()
    max_bh_size = models.IntegerField()
    key_deposit = models.DecimalField(max_digits=20, decimal_places=0)
    pool_deposit = models.DecimalField(max_digits=20, decimal_places=0)
    max_epoch = models.IntegerField()
    optimal_pool_count = models.IntegerField()
    influence = models.FloatField()
    monetary_expand_rate = models.FloatField()
    treasury_growth_rate = models.FloatField()
    decentralisation = models.FloatField()
    entropy = models.BinaryField(blank=True, null=True)
    protocol_major = models.IntegerField()
    protocol_minor = models.IntegerField()
    min_utxo_value = models.DecimalField(max_digits=20, decimal_places=0)
    min_pool_cost = models.DecimalField(max_digits=20, decimal_places=0)
    nonce = models.BinaryField(blank=True, null=True)
    coins_per_utxo_word = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    cost_model = models.ForeignKey(CostModel, models.DO_NOTHING, blank=True, null=True)
    price_mem = models.FloatField(blank=True, null=True)
    price_step = models.FloatField(blank=True, null=True)
    max_tx_ex_mem = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_tx_ex_steps = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_block_ex_mem = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_block_ex_steps = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_val_size = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    collateral_percent = models.IntegerField(blank=True, null=True)
    max_collateral_inputs = models.IntegerField(blank=True, null=True)
    block = models.ForeignKey(Block, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'epoch_param'
        unique_together = (('epoch_no', 'block'),)


class EpochRewardTotalReceived(models.Model):
    id = models.BigAutoField(primary_key=True)
    earned_epoch = models.IntegerField(unique=True)
    amount = models.DecimalField(max_digits=20, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'epoch_reward_total_received'


class EpochStake(models.Model):
    id = models.BigAutoField(primary_key=True)
    addr = models.ForeignKey('StakeAddress', models.DO_NOTHING)
    pool = models.ForeignKey('PoolHash', models.DO_NOTHING)
    amount = models.DecimalField(max_digits=20, decimal_places=0)
    epoch_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'epoch_stake'
        unique_together = (('epoch_no', 'addr', 'pool'),)


class EpochSyncTime(models.Model):
    id = models.BigAutoField(primary_key=True)
    no = models.BigIntegerField(unique=True)
    seconds = models.BigIntegerField()
    state = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'epoch_sync_time'


class MaTxMint(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=20, decimal_places=0)
    tx = models.ForeignKey('Tx', models.DO_NOTHING)
    ident = models.ForeignKey('MultiAsset', models.DO_NOTHING, db_column='ident')

    class Meta:
        managed = False
        db_table = 'ma_tx_mint'
        unique_together = (('ident', 'tx'),)


class MaTxOut(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=20, decimal_places=0)
    tx_out = models.ForeignKey('TxOut', models.DO_NOTHING)
    ident = models.ForeignKey('MultiAsset', models.DO_NOTHING, db_column='ident')

    class Meta:
        managed = False
        db_table = 'ma_tx_out'
        unique_together = (('ident', 'tx_out'),)


class Meta(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_time = models.DateTimeField(unique=True)
    network_name = models.CharField(max_length=-1)
    version = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'meta'


class MultiAsset(models.Model):
    id = models.BigAutoField(primary_key=True)
    policy = models.BinaryField()
    name = models.BinaryField()
    fingerprint = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'multi_asset'
        unique_together = (('policy', 'name'),)


class ParamProposal(models.Model):
    id = models.BigAutoField(primary_key=True)
    epoch_no = models.IntegerField()
    key = models.BinaryField()
    min_fee_a = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    min_fee_b = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_block_size = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_tx_size = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_bh_size = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    key_deposit = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    pool_deposit = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_epoch = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    optimal_pool_count = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    influence = models.FloatField(blank=True, null=True)
    monetary_expand_rate = models.FloatField(blank=True, null=True)
    treasury_growth_rate = models.FloatField(blank=True, null=True)
    decentralisation = models.FloatField(blank=True, null=True)
    entropy = models.BinaryField(blank=True, null=True)
    protocol_major = models.IntegerField(blank=True, null=True)
    protocol_minor = models.IntegerField(blank=True, null=True)
    min_utxo_value = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    min_pool_cost = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    coins_per_utxo_word = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    cost_model = models.ForeignKey(CostModel, models.DO_NOTHING, blank=True, null=True)
    price_mem = models.FloatField(blank=True, null=True)
    price_step = models.FloatField(blank=True, null=True)
    max_tx_ex_mem = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_tx_ex_steps = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_block_ex_mem = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_block_ex_steps = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_val_size = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    collateral_percent = models.IntegerField(blank=True, null=True)
    max_collateral_inputs = models.IntegerField(blank=True, null=True)
    registered_tx = models.ForeignKey('Tx', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'param_proposal'
        unique_together = (('key', 'registered_tx'),)


class PoolHash(models.Model):
    id = models.BigAutoField(primary_key=True)
    hash_raw = models.BinaryField(unique=True)
    view = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'pool_hash'


class PoolMetadataRef(models.Model):
    id = models.BigAutoField(primary_key=True)
    pool = models.ForeignKey(PoolHash, models.DO_NOTHING)
    url = models.CharField(max_length=-1)
    hash = models.BinaryField()
    registered_tx = models.ForeignKey('Tx', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pool_metadata_ref'
        unique_together = (('pool', 'url', 'hash'),)


class PoolOfflineData(models.Model):
    id = models.BigAutoField(primary_key=True)
    pool = models.ForeignKey(PoolHash, models.DO_NOTHING)
    ticker_name = models.CharField(max_length=-1)
    hash = models.BinaryField()
    json = models.JSONField()
    bytes = models.BinaryField()
    pmr = models.ForeignKey(PoolMetadataRef, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pool_offline_data'
        unique_together = (('pool', 'hash'),)


class PoolOfflineFetchError(models.Model):
    id = models.BigAutoField(primary_key=True)
    pool = models.ForeignKey(PoolHash, models.DO_NOTHING)
    fetch_time = models.DateTimeField()
    pmr = models.ForeignKey(PoolMetadataRef, models.DO_NOTHING)
    fetch_error = models.CharField(max_length=-1)
    retry_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pool_offline_fetch_error'
        unique_together = (('pool', 'fetch_time', 'retry_count'),)


class PoolOwner(models.Model):
    id = models.BigAutoField(primary_key=True)
    addr = models.ForeignKey('StakeAddress', models.DO_NOTHING)
    pool_hash = models.ForeignKey(PoolHash, models.DO_NOTHING)
    registered_tx = models.ForeignKey('Tx', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pool_owner'
        unique_together = (('addr', 'pool_hash', 'registered_tx'),)


class PoolRelay(models.Model):
    id = models.BigAutoField(primary_key=True)
    update = models.ForeignKey('PoolUpdate', models.DO_NOTHING)
    ipv4 = models.CharField(max_length=-1, blank=True, null=True)
    ipv6 = models.CharField(max_length=-1, blank=True, null=True)
    dns_name = models.CharField(max_length=-1, blank=True, null=True)
    dns_srv_name = models.CharField(max_length=-1, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pool_relay'
        unique_together = (('update', 'ipv4', 'ipv6', 'dns_name'),)


class PoolRetire(models.Model):
    id = models.BigAutoField(primary_key=True)
    hash = models.ForeignKey(PoolHash, models.DO_NOTHING)
    cert_index = models.IntegerField()
    announced_tx = models.ForeignKey('Tx', models.DO_NOTHING)
    retiring_epoch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pool_retire'
        unique_together = (('hash', 'announced_tx'),)


class PoolUpdate(models.Model):
    id = models.BigAutoField(primary_key=True)
    hash = models.ForeignKey(PoolHash, models.DO_NOTHING)
    cert_index = models.IntegerField()
    vrf_key_hash = models.BinaryField()
    pledge = models.DecimalField(max_digits=20, decimal_places=0)
    reward_addr = models.BinaryField()
    active_epoch_no = models.BigIntegerField()
    meta = models.ForeignKey(PoolMetadataRef, models.DO_NOTHING, blank=True, null=True)
    margin = models.FloatField()
    fixed_cost = models.DecimalField(max_digits=20, decimal_places=0)
    registered_tx = models.ForeignKey('Tx', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pool_update'
        unique_together = (('hash', 'registered_tx'),)


class PotTransfer(models.Model):
    id = models.BigAutoField(primary_key=True)
    cert_index = models.IntegerField()
    treasury = models.DecimalField(max_digits=20, decimal_places=0)
    reserves = models.DecimalField(max_digits=20, decimal_places=0)
    tx = models.ForeignKey('Tx', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pot_transfer'
        unique_together = (('tx', 'cert_index'),)


class Redeemer(models.Model):
    id = models.BigAutoField(primary_key=True)
    tx = models.ForeignKey('Tx', models.DO_NOTHING)
    unit_mem = models.BigIntegerField()
    unit_steps = models.BigIntegerField()
    fee = models.DecimalField(max_digits=20, decimal_places=0)
    purpose = models.TextField()  # This field type is a guess.
    index = models.IntegerField()
    script_hash = models.BinaryField(blank=True, null=True)
    datum = models.ForeignKey(Datum, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'redeemer'
        unique_together = (('tx', 'purpose', 'index'),)


class Reserve(models.Model):
    id = models.BigAutoField(primary_key=True)
    addr = models.ForeignKey('StakeAddress', models.DO_NOTHING)
    cert_index = models.IntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=0)
    tx = models.ForeignKey('Tx', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reserve'
        unique_together = (('addr', 'tx'),)


class ReservedPoolTicker(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=-1)
    pool_hash = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'reserved_pool_ticker'


class Reward(models.Model):
    id = models.BigAutoField(primary_key=True)
    addr = models.ForeignKey('StakeAddress', models.DO_NOTHING)
    type = models.TextField()  # This field type is a guess.
    amount = models.DecimalField(max_digits=20, decimal_places=0)
    earned_epoch = models.BigIntegerField()
    spendable_epoch = models.BigIntegerField()
    pool = models.ForeignKey(PoolHash, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reward'
        unique_together = (('addr', 'type', 'earned_epoch', 'pool'),)


class SchemaVersion(models.Model):
    id = models.BigAutoField(primary_key=True)
    stage_one = models.BigIntegerField()
    stage_two = models.BigIntegerField()
    stage_three = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'schema_version'


class Script(models.Model):
    id = models.BigAutoField(primary_key=True)
    tx = models.ForeignKey('Tx', models.DO_NOTHING)
    hash = models.BinaryField(unique=True)
    type = models.TextField()  # This field type is a guess.
    json = models.JSONField(blank=True, null=True)
    bytes = models.BinaryField(blank=True, null=True)
    serialised_size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'script'


class SlotLeader(models.Model):
    id = models.BigAutoField(primary_key=True)
    hash = models.BinaryField(unique=True)
    pool_hash = models.ForeignKey(PoolHash, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'slot_leader'


class StakeAddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    hash_raw = models.BinaryField(unique=True)
    view = models.CharField(max_length=-1)
    script_hash = models.BinaryField(blank=True, null=True)
    registered_tx = models.ForeignKey('Tx', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stake_address'


class StakeDeregistration(models.Model):
    id = models.BigAutoField(primary_key=True)
    addr = models.ForeignKey(StakeAddress, models.DO_NOTHING)
    cert_index = models.IntegerField()
    epoch_no = models.IntegerField()
    tx = models.ForeignKey('Tx', models.DO_NOTHING)
    redeemer = models.ForeignKey(Redeemer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stake_deregistration'
        unique_together = (('addr', 'tx'),)


class StakeRegistration(models.Model):
    id = models.BigAutoField(primary_key=True)
    addr = models.ForeignKey(StakeAddress, models.DO_NOTHING)
    cert_index = models.IntegerField()
    epoch_no = models.IntegerField()
    tx = models.ForeignKey('Tx', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stake_registration'
        unique_together = (('addr', 'tx'),)


class Treasury(models.Model):
    id = models.BigAutoField(primary_key=True)
    addr = models.ForeignKey(StakeAddress, models.DO_NOTHING)
    cert_index = models.IntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=0)
    tx = models.ForeignKey('Tx', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'treasury'
        unique_together = (('addr', 'tx'),)


class Tx(models.Model):
    id = models.BigAutoField(primary_key=True)
    hash = models.BinaryField(unique=True)
    block = models.ForeignKey(Block, models.DO_NOTHING)
    block_index = models.IntegerField()
    out_sum = models.DecimalField(max_digits=20, decimal_places=0)
    fee = models.DecimalField(max_digits=20, decimal_places=0)
    deposit = models.BigIntegerField()
    size = models.IntegerField()
    invalid_before = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    invalid_hereafter = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    valid_contract = models.BooleanField()
    script_size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tx'


class TxIn(models.Model):
    id = models.BigAutoField(primary_key=True)
    tx_in = models.ForeignKey(Tx, models.DO_NOTHING)
    tx_out = models.ForeignKey(Tx, models.DO_NOTHING)
    tx_out_index = models.SmallIntegerField()
    redeemer = models.ForeignKey(Redeemer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tx_in'
        unique_together = (('tx_out', 'tx_out_index'),)


class TxMetadata(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.DecimalField(max_digits=20, decimal_places=0)
    json = models.JSONField(blank=True, null=True)
    bytes = models.BinaryField()
    tx = models.ForeignKey(Tx, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tx_metadata'
        unique_together = (('key', 'tx'),)


class TxOut(models.Model):
    id = models.BigAutoField(primary_key=True)
    tx = models.ForeignKey(Tx, models.DO_NOTHING)
    index = models.SmallIntegerField()
    address = models.CharField(max_length=-1)
    address_raw = models.BinaryField()
    address_has_script = models.BooleanField()
    payment_cred = models.BinaryField(blank=True, null=True)
    stake_address = models.ForeignKey(StakeAddress, models.DO_NOTHING, blank=True, null=True)
    value = models.DecimalField(max_digits=20, decimal_places=0)
    data_hash = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tx_out'
        unique_together = (('tx', 'index'),)


class Withdrawal(models.Model):
    id = models.BigAutoField(primary_key=True)
    addr = models.ForeignKey(StakeAddress, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=20, decimal_places=0)
    redeemer = models.ForeignKey(Redeemer, models.DO_NOTHING, blank=True, null=True)
    tx = models.ForeignKey(Tx, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'withdrawal'
        unique_together = (('addr', 'tx'),)
