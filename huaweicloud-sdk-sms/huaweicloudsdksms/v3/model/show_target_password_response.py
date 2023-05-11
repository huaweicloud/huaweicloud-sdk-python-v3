# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTargetPasswordResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'target_password': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'target_password': 'target_password'
    }

    def __init__(self, template_id=None, target_password=None):
        """ShowTargetPasswordResponse

        The model defined in huaweicloud sdk

        :param template_id: 模板ID
        :type template_id: str
        :param target_password: 目的端密码
        :type target_password: str
        """
        
        super(ShowTargetPasswordResponse, self).__init__()

        self._template_id = None
        self._target_password = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if target_password is not None:
            self.target_password = target_password

    @property
    def template_id(self):
        """Gets the template_id of this ShowTargetPasswordResponse.

        模板ID

        :return: The template_id of this ShowTargetPasswordResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ShowTargetPasswordResponse.

        模板ID

        :param template_id: The template_id of this ShowTargetPasswordResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def target_password(self):
        """Gets the target_password of this ShowTargetPasswordResponse.

        目的端密码

        :return: The target_password of this ShowTargetPasswordResponse.
        :rtype: str
        """
        return self._target_password

    @target_password.setter
    def target_password(self, target_password):
        """Sets the target_password of this ShowTargetPasswordResponse.

        目的端密码

        :param target_password: The target_password of this ShowTargetPasswordResponse.
        :type target_password: str
        """
        self._target_password = target_password

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
        if not isinstance(other, ShowTargetPasswordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
