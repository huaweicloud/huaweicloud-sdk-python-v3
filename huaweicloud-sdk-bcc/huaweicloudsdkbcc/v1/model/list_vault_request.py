# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVaultRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'region_id': 'str',
        'enterprise_project_id': 'str',
        'compliance_id': 'str',
        'policy_id': 'str',
        'resource_ids': 'str',
        'status': 'str',
        'object_type': 'str',
        'protect_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'enterprise_project_id': 'enterprise_project_id',
        'compliance_id': 'compliance_id',
        'policy_id': 'policy_id',
        'resource_ids': 'resource_ids',
        'status': 'status',
        'object_type': 'object_type',
        'protect_type': 'protect_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, domain_id=None, region_id=None, enterprise_project_id=None, compliance_id=None, policy_id=None, resource_ids=None, status=None, object_type=None, protect_type=None, limit=None, offset=None):
        r"""ListVaultRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param region_id: 归属region
        :type region_id: str
        :param enterprise_project_id: 企业项目id或all_granted_eps，all_granted_eps表示查询用户有权限的所有企业项目id
        :type enterprise_project_id: str
        :param compliance_id: 合规id
        :type compliance_id: str
        :param policy_id: 策略ID
        :type policy_id: str
        :param resource_ids: 资源id，支持多资源，以英文逗号分隔
        :type resource_ids: str
        :param status: 状态，available可用，lock锁定，frozen冻结，error错误，deleting删除中
        :type status: str
        :param object_type: 存储库存储类型，server云服务器，disk磁盘，turbo，workspace云空间，vmware，rds，file
        :type object_type: str
        :param protect_type: 存储库保护类型，backup：备份，replication：复制
        :type protect_type: str
        :param limit: 每页显示条目数，正整数
        :type limit: int
        :param offset: 偏移值,正整数
        :type offset: int
        """
        
        

        self._domain_id = None
        self._region_id = None
        self._enterprise_project_id = None
        self._compliance_id = None
        self._policy_id = None
        self._resource_ids = None
        self._status = None
        self._object_type = None
        self._protect_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if compliance_id is not None:
            self.compliance_id = compliance_id
        if policy_id is not None:
            self.policy_id = policy_id
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if status is not None:
            self.status = status
        if object_type is not None:
            self.object_type = object_type
        if protect_type is not None:
            self.protect_type = protect_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListVaultRequest.

        账号ID

        :return: The domain_id of this ListVaultRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListVaultRequest.

        账号ID

        :param domain_id: The domain_id of this ListVaultRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ListVaultRequest.

        归属region

        :return: The region_id of this ListVaultRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListVaultRequest.

        归属region

        :param region_id: The region_id of this ListVaultRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVaultRequest.

        企业项目id或all_granted_eps，all_granted_eps表示查询用户有权限的所有企业项目id

        :return: The enterprise_project_id of this ListVaultRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVaultRequest.

        企业项目id或all_granted_eps，all_granted_eps表示查询用户有权限的所有企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListVaultRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def compliance_id(self):
        r"""Gets the compliance_id of this ListVaultRequest.

        合规id

        :return: The compliance_id of this ListVaultRequest.
        :rtype: str
        """
        return self._compliance_id

    @compliance_id.setter
    def compliance_id(self, compliance_id):
        r"""Sets the compliance_id of this ListVaultRequest.

        合规id

        :param compliance_id: The compliance_id of this ListVaultRequest.
        :type compliance_id: str
        """
        self._compliance_id = compliance_id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListVaultRequest.

        策略ID

        :return: The policy_id of this ListVaultRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListVaultRequest.

        策略ID

        :param policy_id: The policy_id of this ListVaultRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this ListVaultRequest.

        资源id，支持多资源，以英文逗号分隔

        :return: The resource_ids of this ListVaultRequest.
        :rtype: str
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this ListVaultRequest.

        资源id，支持多资源，以英文逗号分隔

        :param resource_ids: The resource_ids of this ListVaultRequest.
        :type resource_ids: str
        """
        self._resource_ids = resource_ids

    @property
    def status(self):
        r"""Gets the status of this ListVaultRequest.

        状态，available可用，lock锁定，frozen冻结，error错误，deleting删除中

        :return: The status of this ListVaultRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVaultRequest.

        状态，available可用，lock锁定，frozen冻结，error错误，deleting删除中

        :param status: The status of this ListVaultRequest.
        :type status: str
        """
        self._status = status

    @property
    def object_type(self):
        r"""Gets the object_type of this ListVaultRequest.

        存储库存储类型，server云服务器，disk磁盘，turbo，workspace云空间，vmware，rds，file

        :return: The object_type of this ListVaultRequest.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ListVaultRequest.

        存储库存储类型，server云服务器，disk磁盘，turbo，workspace云空间，vmware，rds，file

        :param object_type: The object_type of this ListVaultRequest.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def protect_type(self):
        r"""Gets the protect_type of this ListVaultRequest.

        存储库保护类型，backup：备份，replication：复制

        :return: The protect_type of this ListVaultRequest.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        r"""Sets the protect_type of this ListVaultRequest.

        存储库保护类型，backup：备份，replication：复制

        :param protect_type: The protect_type of this ListVaultRequest.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def limit(self):
        r"""Gets the limit of this ListVaultRequest.

        每页显示条目数，正整数

        :return: The limit of this ListVaultRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVaultRequest.

        每页显示条目数，正整数

        :param limit: The limit of this ListVaultRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListVaultRequest.

        偏移值,正整数

        :return: The offset of this ListVaultRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVaultRequest.

        偏移值,正整数

        :param offset: The offset of this ListVaultRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListVaultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
