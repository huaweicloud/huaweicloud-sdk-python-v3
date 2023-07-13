# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcMemberModify:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'members': 'list[MemberInfo]',
        'member_group_name': 'str'
    }

    attribute_map = {
        'members': 'members',
        'member_group_name': 'member_group_name'
    }

    def __init__(self, members=None, member_group_name=None):
        """VpcMemberModify

        The model defined in huaweicloud sdk

        :param members: 后端实例列表
        :type members: list[:class:`huaweicloudsdkapig.v2.MemberInfo`]
        :param member_group_name: 需要修改的后端服务器组  不传时使用members中的定义对VPC通道后端进行全量覆盖修改。  传入时，只对members中对应后端服务器组的后端实例进行处理，其他后端服务器组的入参会被忽略。例如：member_group_name&#x3D;primary时，只处理members中后端服务器组为105c6902457144a4820dff8b1ad63331的后端实例。
        :type member_group_name: str
        """
        
        

        self._members = None
        self._member_group_name = None
        self.discriminator = None

        if members is not None:
            self.members = members
        if member_group_name is not None:
            self.member_group_name = member_group_name

    @property
    def members(self):
        """Gets the members of this VpcMemberModify.

        后端实例列表

        :return: The members of this VpcMemberModify.
        :rtype: list[:class:`huaweicloudsdkapig.v2.MemberInfo`]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this VpcMemberModify.

        后端实例列表

        :param members: The members of this VpcMemberModify.
        :type members: list[:class:`huaweicloudsdkapig.v2.MemberInfo`]
        """
        self._members = members

    @property
    def member_group_name(self):
        """Gets the member_group_name of this VpcMemberModify.

        需要修改的后端服务器组  不传时使用members中的定义对VPC通道后端进行全量覆盖修改。  传入时，只对members中对应后端服务器组的后端实例进行处理，其他后端服务器组的入参会被忽略。例如：member_group_name=primary时，只处理members中后端服务器组为105c6902457144a4820dff8b1ad63331的后端实例。

        :return: The member_group_name of this VpcMemberModify.
        :rtype: str
        """
        return self._member_group_name

    @member_group_name.setter
    def member_group_name(self, member_group_name):
        """Sets the member_group_name of this VpcMemberModify.

        需要修改的后端服务器组  不传时使用members中的定义对VPC通道后端进行全量覆盖修改。  传入时，只对members中对应后端服务器组的后端实例进行处理，其他后端服务器组的入参会被忽略。例如：member_group_name=primary时，只处理members中后端服务器组为105c6902457144a4820dff8b1ad63331的后端实例。

        :param member_group_name: The member_group_name of this VpcMemberModify.
        :type member_group_name: str
        """
        self._member_group_name = member_group_name

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
        if not isinstance(other, VpcMemberModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
