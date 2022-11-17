# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMemberRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'user_id': 'str',
        'body': 'UpdateMemberReq'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'user_id': 'user_id',
        'body': 'body'
    }

    def __init__(self, eihealth_project_id=None, user_id=None, body=None):
        """UpdateMemberRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param user_id: 更新或者添加项目成员角色的用户id
        :type user_id: str
        :param body: Body of the UpdateMemberRequest
        :type body: :class:`huaweicloudsdkeihealth.v1.UpdateMemberReq`
        """
        
        

        self._eihealth_project_id = None
        self._user_id = None
        self._body = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        self.user_id = user_id
        if body is not None:
            self.body = body

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this UpdateMemberRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this UpdateMemberRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this UpdateMemberRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this UpdateMemberRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def user_id(self):
        """Gets the user_id of this UpdateMemberRequest.

        更新或者添加项目成员角色的用户id

        :return: The user_id of this UpdateMemberRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UpdateMemberRequest.

        更新或者添加项目成员角色的用户id

        :param user_id: The user_id of this UpdateMemberRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def body(self):
        """Gets the body of this UpdateMemberRequest.

        :return: The body of this UpdateMemberRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMemberReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateMemberRequest.

        :param body: The body of this UpdateMemberRequest.
        :type body: :class:`huaweicloudsdkeihealth.v1.UpdateMemberReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateMemberRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
