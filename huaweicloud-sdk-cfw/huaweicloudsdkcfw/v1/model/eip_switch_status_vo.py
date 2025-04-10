# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EIPSwitchStatusVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'fail_eip_id_list': 'list[str]',
        'fail_eip_list': 'list[FailedEipInfo]',
        'id': 'str'
    }

    attribute_map = {
        'object_id': 'object_id',
        'fail_eip_id_list': 'fail_eip_id_list',
        'fail_eip_list': 'fail_eip_list',
        'id': 'id'
    }

    def __init__(self, object_id=None, fail_eip_id_list=None, fail_eip_list=None, id=None):
        r"""EIPSwitchStatusVO

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为0的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得
        :type object_id: str
        :param fail_eip_id_list: 修改eip防护状态失败状态列表，状态包括成功\&quot;successful\&quot;，失败“fail”
        :type fail_eip_id_list: list[str]
        :param fail_eip_list: 修改eip防护状态失败信息列表
        :type fail_eip_list: list[:class:`huaweicloudsdkcfw.v1.FailedEipInfo`]
        :param id: 防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type id: str
        """
        
        

        self._object_id = None
        self._fail_eip_id_list = None
        self._fail_eip_list = None
        self._id = None
        self.discriminator = None

        if object_id is not None:
            self.object_id = object_id
        if fail_eip_id_list is not None:
            self.fail_eip_id_list = fail_eip_id_list
        if fail_eip_list is not None:
            self.fail_eip_list = fail_eip_list
        if id is not None:
            self.id = id

    @property
    def object_id(self):
        r"""Gets the object_id of this EIPSwitchStatusVO.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为0的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :return: The object_id of this EIPSwitchStatusVO.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this EIPSwitchStatusVO.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为0的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :param object_id: The object_id of this EIPSwitchStatusVO.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def fail_eip_id_list(self):
        r"""Gets the fail_eip_id_list of this EIPSwitchStatusVO.

        修改eip防护状态失败状态列表，状态包括成功\"successful\"，失败“fail”

        :return: The fail_eip_id_list of this EIPSwitchStatusVO.
        :rtype: list[str]
        """
        return self._fail_eip_id_list

    @fail_eip_id_list.setter
    def fail_eip_id_list(self, fail_eip_id_list):
        r"""Sets the fail_eip_id_list of this EIPSwitchStatusVO.

        修改eip防护状态失败状态列表，状态包括成功\"successful\"，失败“fail”

        :param fail_eip_id_list: The fail_eip_id_list of this EIPSwitchStatusVO.
        :type fail_eip_id_list: list[str]
        """
        self._fail_eip_id_list = fail_eip_id_list

    @property
    def fail_eip_list(self):
        r"""Gets the fail_eip_list of this EIPSwitchStatusVO.

        修改eip防护状态失败信息列表

        :return: The fail_eip_list of this EIPSwitchStatusVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.FailedEipInfo`]
        """
        return self._fail_eip_list

    @fail_eip_list.setter
    def fail_eip_list(self, fail_eip_list):
        r"""Sets the fail_eip_list of this EIPSwitchStatusVO.

        修改eip防护状态失败信息列表

        :param fail_eip_list: The fail_eip_list of this EIPSwitchStatusVO.
        :type fail_eip_list: list[:class:`huaweicloudsdkcfw.v1.FailedEipInfo`]
        """
        self._fail_eip_list = fail_eip_list

    @property
    def id(self):
        r"""Gets the id of this EIPSwitchStatusVO.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The id of this EIPSwitchStatusVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EIPSwitchStatusVO.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param id: The id of this EIPSwitchStatusVO.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, EIPSwitchStatusVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
