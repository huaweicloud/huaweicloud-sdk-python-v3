# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteBlackWhiteListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'list_id': 'str',
        'enterprise_project_id': 'str',
        'fw_instance_id': 'str'
    }

    attribute_map = {
        'list_id': 'list_id',
        'enterprise_project_id': 'enterprise_project_id',
        'fw_instance_id': 'fw_instance_id'
    }

    def __init__(self, list_id=None, enterprise_project_id=None, fw_instance_id=None):
        r"""DeleteBlackWhiteListRequest

        The model defined in huaweicloud sdk

        :param list_id: 黑白名单列表id，可通过[查询黑白名单列表接口](ListBlackWhiteLists.xml)查询获得，通过返回值中的data.records.list_id（.表示各对象之间层级的区分）获得。
        :type list_id: str
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        :param fw_instance_id: 防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        """
        
        

        self._list_id = None
        self._enterprise_project_id = None
        self._fw_instance_id = None
        self.discriminator = None

        self.list_id = list_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id

    @property
    def list_id(self):
        r"""Gets the list_id of this DeleteBlackWhiteListRequest.

        黑白名单列表id，可通过[查询黑白名单列表接口](ListBlackWhiteLists.xml)查询获得，通过返回值中的data.records.list_id（.表示各对象之间层级的区分）获得。

        :return: The list_id of this DeleteBlackWhiteListRequest.
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        r"""Sets the list_id of this DeleteBlackWhiteListRequest.

        黑白名单列表id，可通过[查询黑白名单列表接口](ListBlackWhiteLists.xml)查询获得，通过返回值中的data.records.list_id（.表示各对象之间层级的区分）获得。

        :param list_id: The list_id of this DeleteBlackWhiteListRequest.
        :type list_id: str
        """
        self._list_id = list_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this DeleteBlackWhiteListRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this DeleteBlackWhiteListRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this DeleteBlackWhiteListRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this DeleteBlackWhiteListRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this DeleteBlackWhiteListRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this DeleteBlackWhiteListRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this DeleteBlackWhiteListRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this DeleteBlackWhiteListRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

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
        if not isinstance(other, DeleteBlackWhiteListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
