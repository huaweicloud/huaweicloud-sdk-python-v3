# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCorpGroupDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_name': 'str',
        'group_type': 'int',
        'remarks': 'str',
        'region_id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'group_id': 'groupId',
        'group_name': 'groupName',
        'group_type': 'groupType',
        'remarks': 'remarks',
        'region_id': 'regionId',
        'status': 'status'
    }

    def __init__(self, group_id=None, group_name=None, group_type=None, remarks=None, region_id=None, status=None):
        r"""QueryCorpGroupDTO

        The model defined in huaweicloud sdk

        :param group_id: 媒体接入分组id。
        :type group_id: str
        :param group_name: 分组名称。
        :type group_name: str
        :param group_type: 分组类型。
        :type group_type: int
        :param remarks: 分组备注信息。
        :type remarks: str
        :param region_id: 区域ID，仅服务列表类型场景必填。
        :type region_id: str
        :param status: 分组状态。 - 0: 正常 - 1: 停用，服务列表类型停用后创建企业就不会再自动分配到该分组 
        :type status: int
        """
        
        

        self._group_id = None
        self._group_name = None
        self._group_type = None
        self._remarks = None
        self._region_id = None
        self._status = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if group_type is not None:
            self.group_type = group_type
        if remarks is not None:
            self.remarks = remarks
        if region_id is not None:
            self.region_id = region_id
        if status is not None:
            self.status = status

    @property
    def group_id(self):
        r"""Gets the group_id of this QueryCorpGroupDTO.

        媒体接入分组id。

        :return: The group_id of this QueryCorpGroupDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this QueryCorpGroupDTO.

        媒体接入分组id。

        :param group_id: The group_id of this QueryCorpGroupDTO.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this QueryCorpGroupDTO.

        分组名称。

        :return: The group_name of this QueryCorpGroupDTO.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this QueryCorpGroupDTO.

        分组名称。

        :param group_name: The group_name of this QueryCorpGroupDTO.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_type(self):
        r"""Gets the group_type of this QueryCorpGroupDTO.

        分组类型。

        :return: The group_type of this QueryCorpGroupDTO.
        :rtype: int
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this QueryCorpGroupDTO.

        分组类型。

        :param group_type: The group_type of this QueryCorpGroupDTO.
        :type group_type: int
        """
        self._group_type = group_type

    @property
    def remarks(self):
        r"""Gets the remarks of this QueryCorpGroupDTO.

        分组备注信息。

        :return: The remarks of this QueryCorpGroupDTO.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this QueryCorpGroupDTO.

        分组备注信息。

        :param remarks: The remarks of this QueryCorpGroupDTO.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def region_id(self):
        r"""Gets the region_id of this QueryCorpGroupDTO.

        区域ID，仅服务列表类型场景必填。

        :return: The region_id of this QueryCorpGroupDTO.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this QueryCorpGroupDTO.

        区域ID，仅服务列表类型场景必填。

        :param region_id: The region_id of this QueryCorpGroupDTO.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def status(self):
        r"""Gets the status of this QueryCorpGroupDTO.

        分组状态。 - 0: 正常 - 1: 停用，服务列表类型停用后创建企业就不会再自动分配到该分组 

        :return: The status of this QueryCorpGroupDTO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryCorpGroupDTO.

        分组状态。 - 0: 正常 - 1: 停用，服务列表类型停用后创建企业就不会再自动分配到该分组 

        :param status: The status of this QueryCorpGroupDTO.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, QueryCorpGroupDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
