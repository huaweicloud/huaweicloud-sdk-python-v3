# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserAccessStagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'username': 'str',
        'biz_type': 'str',
        'stages': 'list[UserAccessStage]'
    }

    attribute_map = {
        'username': 'username',
        'biz_type': 'biz_type',
        'stages': 'stages'
    }

    def __init__(self, username=None, biz_type=None, stages=None):
        r"""ShowUserAccessStagesResponse

        The model defined in huaweicloud sdk

        :param username: 用户名。
        :type username: str
        :param biz_type: 接入阶段 | APP - 应用 DESKTOP - 桌面。
        :type biz_type: str
        :param stages: 接入各阶段详情。
        :type stages: list[:class:`huaweicloudsdkworkspace.v2.UserAccessStage`]
        """
        
        super(ShowUserAccessStagesResponse, self).__init__()

        self._username = None
        self._biz_type = None
        self._stages = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if biz_type is not None:
            self.biz_type = biz_type
        if stages is not None:
            self.stages = stages

    @property
    def username(self):
        r"""Gets the username of this ShowUserAccessStagesResponse.

        用户名。

        :return: The username of this ShowUserAccessStagesResponse.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ShowUserAccessStagesResponse.

        用户名。

        :param username: The username of this ShowUserAccessStagesResponse.
        :type username: str
        """
        self._username = username

    @property
    def biz_type(self):
        r"""Gets the biz_type of this ShowUserAccessStagesResponse.

        接入阶段 | APP - 应用 DESKTOP - 桌面。

        :return: The biz_type of this ShowUserAccessStagesResponse.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this ShowUserAccessStagesResponse.

        接入阶段 | APP - 应用 DESKTOP - 桌面。

        :param biz_type: The biz_type of this ShowUserAccessStagesResponse.
        :type biz_type: str
        """
        self._biz_type = biz_type

    @property
    def stages(self):
        r"""Gets the stages of this ShowUserAccessStagesResponse.

        接入各阶段详情。

        :return: The stages of this ShowUserAccessStagesResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.UserAccessStage`]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        r"""Sets the stages of this ShowUserAccessStagesResponse.

        接入各阶段详情。

        :param stages: The stages of this ShowUserAccessStagesResponse.
        :type stages: list[:class:`huaweicloudsdkworkspace.v2.UserAccessStage`]
        """
        self._stages = stages

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
        if not isinstance(other, ShowUserAccessStagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
