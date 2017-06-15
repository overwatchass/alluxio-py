# -*- coding: utf-8 -*-
"""Options for Alluxio Client methods.

By convention, methods in :class:`alluxio.Client` have a **kwargs** field for
setting optional parameters. For each method, there is a corresponding option
class in this module, which defines the optional parameters that can be set in
that method. You should not need to create these objects manually, they are
automatically created by the methods in :class:`alluxio.Client`.

Examples:
    For :meth:`alluxio.Client.create_directory`, the parameters that
    can be set to **kwargs** are specified in :class:`alluxio.option.CreateDirectory`.

Notes:
    All classes in this module have a **json** method, which converts the class
    into a python dict that can be encoded into a json string.
"""

from .common import _Jsonable


class CreateDirectory(_Jsonable):
    """Options to be used in :meth:`alluxio.Client.create_directory`.

    Args:
        allow_exists (bool): Whether the directory can already exist.
        mode (:obj:`alluxio.wire.Mode`): The directory's access mode.
        recursive (bool): If True, creates intermediate directories along the
            path as necessary.
        write_type (:obj:`alluxio.wire.WriteType`): It can be used to decide
            where the directory will be created, like in Alluxio only, or in
            both Alluxio and under storage.
    """

    def __init__(self, **kwargs):
        self.allow_exists = kwargs.get('allow_exists')
        self.mode = kwargs.get('mode')
        self.recursive = kwargs.get('recursive')
        self.write_type = kwargs.get('write_type')

    def json(self):
        obj = {}
        if self.allow_exists:
            obj['allowExists'] = self.allow_exists
        if self.mode:
            obj['mode'] = self.mode.json()
        if self.recursive:
            obj['recursive'] = self.recursive
        if self.write_type:
            obj['writeType'] = self.write_type.json()
        return obj


class CreateFile(_Jsonable):
    """Options to be used in :meth:`alluxio.Client.create_file`.

    Args:
        block_size_bytes (int): Block size of the file in bytes.
        location_policy_class (str): The Java class name for the location policy.
            If this is not specified, Alluxio will use the default value of the
            property key **alluxio.user.file.write.location.policy.class**.
        mode (:obj:`alluxio.wire.Mode`): The file's access mode.
        recursive (bool): If True, creates intermediate directories along the
            path as necessary.
        ttl (int): The TTL (time to live) value. It identifies duration
            (in milliseconds) the created file should be kept around before it
            is automatically deleted. -1 means no TTL value is set.
        ttl_action (:obj:`alluxio.wire.TTLAction`): The file action to take when
            its TTL expires.
        write_type (:obj:`alluxio.wire.WriteType`): It can be used to decide
            where the file will be created, like in Alluxio only, or in
            both Alluxio and under storage.
    """

    def __init__(self, **kwargs):
        self.block_size_bytes = kwargs.get('block_size_bytes')
        self.location_policy_class = kwargs.get('location_policy_class')
        self.mode = kwargs.get('mode')
        self.recursive = kwargs.get('recursive')
        self.ttl = kwargs.get('ttl')
        self.ttl_action = kwargs.get('ttl_action')
        self.write_type = kwargs.get('write_type')

    def json(self):
        obj = {}
        if self.block_size_bytes:
            obj['blockSizeBytes'] = self.block_size_bytes
        if self.location_policy_class:
            obj['locationPolicyClass'] = self.location_policy_class
        if self.mode:
            obj['mode'] = self.mode.json()
        if self.recursive:
            obj['recursive'] = self.recursive
        if self.ttl:
            obj['ttl'] = self.ttl
        if self.ttl_action:
            obj['ttlAction'] = self.ttl_action.json()
        if self.write_type:
            obj['writeType'] = self.write_type.json()
        return obj


class Delete(_Jsonable):
    """Options to be used in :meth:`alluxio.Client.delete`.

    Args:
        recursive (bool): If set to true for a path to a directory, the
            directory and its contents will be deleted.
    """

    def __init__(self, **kwargs):
        self.recursive = kwargs.get('recursive')

    def json(self):
        obj = {}
        if self.recursive:
            obj['recursive'] = self.recursive
        return obj


class Exists(_Jsonable):
    """Options to be used in :meth:`alluxio.Client.exists`.

    Currently, it is an empty class, options may be added in future releases.
    """

    pass


class Free(_Jsonable):
    """Options to be used in :meth:`alluxio.Client.free`.

    Args:
        recursive (bool): If set to true for a path to a directory, the
            directory and its contents will be freed.
    """

    def __init__(self, **kwargs):
        self.recursive = kwargs.get('recursive')

    def json(self):
        obj = {}
        if self.recursive:
            obj['recursive'] = self.recursive
        return obj


class GetStatus(_Jsonable):
    """Options to be used in :meth:`alluxio.Client.get_status`.

    Currently, it is an empty class, options may be added in future releases.
    """

    pass


class ListStatus(_Jsonable):
    """Options to be used in :meth:`alluxio.Client.list_status`.

    Args:
        load_metadata_type (:class:`alluxio.wire.LoadMetadataType`): The type of
            loading metadata, can be one of
            :data:`alluxio.wire.LOAD_METADATA_TYPE_NEVER`,
            :data:`alluxio.wire.LOAD_METADATA_TYPE_ONCE`,
            :data:`alluxio.wire.LOAD_METADATA_TYPE_ALWAYS`,
            see documentation on :class:`alluxio.wire.LoadMetadataType` for more
            details
    """

    def __init__(self, **kwargs):
        self.load_metadata_type = kwargs.get('load_metadata_type')

    def json(self):
        obj = {}
        if self.load_metadata_type:
            obj['loadMetadataType'] = self.load_metadata_type.json()
        return obj


class Mount(_Jsonable):
    """Options to be used in :meth:`alluxio.Client.mount`.

    Args:
        properties (dict): A dictionary mapping property key strings to value strings.
        read_only (bool): Whether the mount point is read-only.
        shared (bool): Whether the mount point is shared with all Alluxio users.
    """

    def __init__(self, **kwargs):
        self.properties = kwargs.get('properties')
        self.read_only = kwargs.get('read_only')
        self.shared = kwargs.get('shared')

    def json(self):
        obj = {}
        if self.properties:
            obj['properties'] = self.properties
        if self.read_only:
            obj['readOnly'] = self.read_only
        if self.shared:
            obj['shared'] = self.shared
        return obj


class OpenFile(_Jsonable):
    """Options to be used in :meth:`alluxio.Client.open_file`.

    Args:
        cache_location_policy_class (str): The Java class name for the location
            policy to be used when caching the opened file. If this is not
            specified, Alluxio will use the default value of the property
            key **alluxio.user.file.write.location.policy.class**.
        max_ufs_read_concurrency (int): The maximum UFS read concurrency for
            one block on one Alluxio worker.
        read_type (:obj:`alluxio.wire.ReadType`): The read type, like whether
            the file read should be cached, if this is not specified, Alluxio
            will use the default value of the property key
            **alluxio.user.file.readtype.default**.
        ufs_read_location_policy_class (str): The Java class name for the
            location policy to be used when reading from under storage. If this
            is not specified, Alluxio will use the default value of the property
            key **alluxio.user.ufs.block.read.location.policy**.
    """

    def __init__(self, **kwargs):
        self.cache_location_policy_class = kwargs.get(
            'cache_location_policy_class')
        self.max_ufs_read_concurrency = kwargs.get('max_ufs_read_concurrency')
        self.read_type = kwargs.get('read_type')
        self.ufs_read_location_policy_class = kwargs.get(
            'ufs_read_location_policy_class')

    def json(self):
        obj = {}
        if self.cache_location_policy_class:
            obj['cacheLocationPolicyClass'] = self.cache_location_policy_class
        if self.max_ufs_read_concurrency:
            obj['maxUfsReadConcurrency'] = self.max_ufs_read_concurrency
        if self.read_type:
            obj['readType'] = self.read_type.json()
        if self.ufs_read_location_policy_class:
            obj['ufsReadLocationPolicyClass'] = self.ufs_read_location_policy_class
        return obj


class Rename(_Jsonable):
    """Options to be used in :meth:`alluxio.Client.rename`.

    Currently, it is an empty class, options may be added in future releases.
    """

    pass


class SetAttribute(_Jsonable):
    """Options to be used in :meth:`alluxio.Client.set_attribute`.

    Args:
        owner (str): The owner of the path.
        group (str): The group of the path.
        mode (:obj:`alluxio.wire.Mode`): The access mode of the path.
        pinned (bool): Whether the path is pinned in Alluxio, which means it
            should be kept in memory.
        recursive (bool): Whether to set ACL (access control list) recursively
            under a directory.
        ttl (int): The TTL (time to live) value. It identifies duration
            (in milliseconds) the file should be kept around before it is
            automatically deleted. -1 means no TTL value is set.
        ttl_action (:obj:`alluxio.wire.TTLAction`): The file action to take when
            its TTL expires.
    """

    def __init__(self):
        self.owner = None
        self.group = None
        self.mode = None
        self.pinned = None
        self.recursive = None
        self.ttl = None
        self.ttl_action = None

    def json(self):
        obj = {}
        if self.owner:
            obj['owner'] = self.owner
        if self.group:
            obj['group'] = self.group
        if self.mode:
            obj['mode'] = self.mode.json()
        if self.pinned:
            obj['pinned'] = self.pinned
        if self.recursive:
            obj['recursive'] = self.recursive
        if self.ttl:
            obj['ttl'] = self.ttl
        if self.ttl_action:
            obj['ttlAction'] = self.ttl_action.json()
        return obj


class Unmount(_Jsonable):
    """Options to be used in :meth:`alluxio.Client.unmount`.

    Currently, it is an empty class, options may be added in future releases.
    """

    pass
