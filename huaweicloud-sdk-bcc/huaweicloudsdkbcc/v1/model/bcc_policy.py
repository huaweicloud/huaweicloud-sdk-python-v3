# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BccPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protection_type': 'str',
        'id': 'str',
        'enabled': 'bool',
        'cyber': 'str',
        'name': 'str',
        'region_id': 'str',
        'storage_type': 'str',
        'policy_type': 'str',
        'service_type': 'str',
        'cbr_policy_detail': 'CbrPolicyDetail',
        'db_policy_detail': 'DbPolicyDetail'
    }

    attribute_map = {
        'protection_type': 'protection_type',
        'id': 'id',
        'enabled': 'enabled',
        'cyber': 'cyber',
        'name': 'name',
        'region_id': 'region_id',
        'storage_type': 'storage_type',
        'policy_type': 'policy_type',
        'service_type': 'service_type',
        'cbr_policy_detail': 'cbr_policy_detail',
        'db_policy_detail': 'db_policy_detail'
    }

    def __init__(self, protection_type=None, id=None, enabled=None, cyber=None, name=None, region_id=None, storage_type=None, policy_type=None, service_type=None, cbr_policy_detail=None, db_policy_detail=None):
        r"""BccPolicy

        The model defined in huaweicloud sdk

        :param protection_type: 保护类型
        :type protection_type: str
        :param id: 策略ID
        :type id: str
        :param enabled: 是否启用策略
        :type enabled: bool
        :param cyber: 是否启用加密
        :type cyber: str
        :param name: 区域名称
        :type name: str
        :param region_id: 区域ID
        :type region_id: str
        :param storage_type: 存储类型，默认obs
        :type storage_type: str
        :param policy_type: 策略类型
        :type policy_type: str
        :param service_type: 保护服务类型
        :type service_type: str
        :param cbr_policy_detail: 
        :type cbr_policy_detail: :class:`huaweicloudsdkbcc.v1.CbrPolicyDetail`
        :param db_policy_detail: 
        :type db_policy_detail: :class:`huaweicloudsdkbcc.v1.DbPolicyDetail`
        """
        
        

        self._protection_type = None
        self._id = None
        self._enabled = None
        self._cyber = None
        self._name = None
        self._region_id = None
        self._storage_type = None
        self._policy_type = None
        self._service_type = None
        self._cbr_policy_detail = None
        self._db_policy_detail = None
        self.discriminator = None

        if protection_type is not None:
            self.protection_type = protection_type
        if id is not None:
            self.id = id
        if enabled is not None:
            self.enabled = enabled
        if cyber is not None:
            self.cyber = cyber
        if name is not None:
            self.name = name
        if region_id is not None:
            self.region_id = region_id
        if storage_type is not None:
            self.storage_type = storage_type
        if policy_type is not None:
            self.policy_type = policy_type
        if service_type is not None:
            self.service_type = service_type
        if cbr_policy_detail is not None:
            self.cbr_policy_detail = cbr_policy_detail
        if db_policy_detail is not None:
            self.db_policy_detail = db_policy_detail

    @property
    def protection_type(self):
        r"""Gets the protection_type of this BccPolicy.

        保护类型

        :return: The protection_type of this BccPolicy.
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        r"""Sets the protection_type of this BccPolicy.

        保护类型

        :param protection_type: The protection_type of this BccPolicy.
        :type protection_type: str
        """
        self._protection_type = protection_type

    @property
    def id(self):
        r"""Gets the id of this BccPolicy.

        策略ID

        :return: The id of this BccPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BccPolicy.

        策略ID

        :param id: The id of this BccPolicy.
        :type id: str
        """
        self._id = id

    @property
    def enabled(self):
        r"""Gets the enabled of this BccPolicy.

        是否启用策略

        :return: The enabled of this BccPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this BccPolicy.

        是否启用策略

        :param enabled: The enabled of this BccPolicy.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def cyber(self):
        r"""Gets the cyber of this BccPolicy.

        是否启用加密

        :return: The cyber of this BccPolicy.
        :rtype: str
        """
        return self._cyber

    @cyber.setter
    def cyber(self, cyber):
        r"""Sets the cyber of this BccPolicy.

        是否启用加密

        :param cyber: The cyber of this BccPolicy.
        :type cyber: str
        """
        self._cyber = cyber

    @property
    def name(self):
        r"""Gets the name of this BccPolicy.

        区域名称

        :return: The name of this BccPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BccPolicy.

        区域名称

        :param name: The name of this BccPolicy.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        r"""Gets the region_id of this BccPolicy.

        区域ID

        :return: The region_id of this BccPolicy.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this BccPolicy.

        区域ID

        :param region_id: The region_id of this BccPolicy.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def storage_type(self):
        r"""Gets the storage_type of this BccPolicy.

        存储类型，默认obs

        :return: The storage_type of this BccPolicy.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this BccPolicy.

        存储类型，默认obs

        :param storage_type: The storage_type of this BccPolicy.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def policy_type(self):
        r"""Gets the policy_type of this BccPolicy.

        策略类型

        :return: The policy_type of this BccPolicy.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this BccPolicy.

        策略类型

        :param policy_type: The policy_type of this BccPolicy.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def service_type(self):
        r"""Gets the service_type of this BccPolicy.

        保护服务类型

        :return: The service_type of this BccPolicy.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this BccPolicy.

        保护服务类型

        :param service_type: The service_type of this BccPolicy.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def cbr_policy_detail(self):
        r"""Gets the cbr_policy_detail of this BccPolicy.

        :return: The cbr_policy_detail of this BccPolicy.
        :rtype: :class:`huaweicloudsdkbcc.v1.CbrPolicyDetail`
        """
        return self._cbr_policy_detail

    @cbr_policy_detail.setter
    def cbr_policy_detail(self, cbr_policy_detail):
        r"""Sets the cbr_policy_detail of this BccPolicy.

        :param cbr_policy_detail: The cbr_policy_detail of this BccPolicy.
        :type cbr_policy_detail: :class:`huaweicloudsdkbcc.v1.CbrPolicyDetail`
        """
        self._cbr_policy_detail = cbr_policy_detail

    @property
    def db_policy_detail(self):
        r"""Gets the db_policy_detail of this BccPolicy.

        :return: The db_policy_detail of this BccPolicy.
        :rtype: :class:`huaweicloudsdkbcc.v1.DbPolicyDetail`
        """
        return self._db_policy_detail

    @db_policy_detail.setter
    def db_policy_detail(self, db_policy_detail):
        r"""Sets the db_policy_detail of this BccPolicy.

        :param db_policy_detail: The db_policy_detail of this BccPolicy.
        :type db_policy_detail: :class:`huaweicloudsdkbcc.v1.DbPolicyDetail`
        """
        self._db_policy_detail = db_policy_detail

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BccPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
