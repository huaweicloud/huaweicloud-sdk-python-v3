# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'group_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'container_mode': 'bool',
        'group_id': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'group_name': 'group_name',
        'offset': 'offset',
        'limit': 'limit',
        'container_mode': 'container_mode',
        'group_id': 'group_id'
    }

    def __init__(self, region=None, enterprise_project_id=None, group_name=None, offset=None, limit=None, container_mode=None, group_id=None):
        r"""ListPolicyGroupRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param group_name: 策略组名
        :type group_name: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param container_mode: 是否查询容器版策略
        :type container_mode: bool
        :param group_id: 策略组id
        :type group_id: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._group_name = None
        self._offset = None
        self._limit = None
        self._container_mode = None
        self._group_id = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if group_name is not None:
            self.group_name = group_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if container_mode is not None:
            self.container_mode = container_mode
        if group_id is not None:
            self.group_id = group_id

    @property
    def region(self):
        r"""Gets the region of this ListPolicyGroupRequest.

        Region ID

        :return: The region of this ListPolicyGroupRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListPolicyGroupRequest.

        Region ID

        :param region: The region of this ListPolicyGroupRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPolicyGroupRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListPolicyGroupRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPolicyGroupRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListPolicyGroupRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ListPolicyGroupRequest.

        策略组名

        :return: The group_name of this ListPolicyGroupRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListPolicyGroupRequest.

        策略组名

        :param group_name: The group_name of this ListPolicyGroupRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def offset(self):
        r"""Gets the offset of this ListPolicyGroupRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListPolicyGroupRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPolicyGroupRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListPolicyGroupRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPolicyGroupRequest.

        每页显示个数

        :return: The limit of this ListPolicyGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPolicyGroupRequest.

        每页显示个数

        :param limit: The limit of this ListPolicyGroupRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def container_mode(self):
        r"""Gets the container_mode of this ListPolicyGroupRequest.

        是否查询容器版策略

        :return: The container_mode of this ListPolicyGroupRequest.
        :rtype: bool
        """
        return self._container_mode

    @container_mode.setter
    def container_mode(self, container_mode):
        r"""Sets the container_mode of this ListPolicyGroupRequest.

        是否查询容器版策略

        :param container_mode: The container_mode of this ListPolicyGroupRequest.
        :type container_mode: bool
        """
        self._container_mode = container_mode

    @property
    def group_id(self):
        r"""Gets the group_id of this ListPolicyGroupRequest.

        策略组id

        :return: The group_id of this ListPolicyGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListPolicyGroupRequest.

        策略组id

        :param group_id: The group_id of this ListPolicyGroupRequest.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, ListPolicyGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
