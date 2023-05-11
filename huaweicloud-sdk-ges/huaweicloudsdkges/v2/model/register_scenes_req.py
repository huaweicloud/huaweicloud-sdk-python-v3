# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterScenesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scenes': 'list[RegisterScenesReqScenes]'
    }

    attribute_map = {
        'scenes': 'scenes'
    }

    def __init__(self, scenes=None):
        """RegisterScenesReq

        The model defined in huaweicloud sdk

        :param scenes: 要订阅的具体场景。
        :type scenes: list[:class:`huaweicloudsdkges.v2.RegisterScenesReqScenes`]
        """
        
        

        self._scenes = None
        self.discriminator = None

        if scenes is not None:
            self.scenes = scenes

    @property
    def scenes(self):
        """Gets the scenes of this RegisterScenesReq.

        要订阅的具体场景。

        :return: The scenes of this RegisterScenesReq.
        :rtype: list[:class:`huaweicloudsdkges.v2.RegisterScenesReqScenes`]
        """
        return self._scenes

    @scenes.setter
    def scenes(self, scenes):
        """Sets the scenes of this RegisterScenesReq.

        要订阅的具体场景。

        :param scenes: The scenes of this RegisterScenesReq.
        :type scenes: list[:class:`huaweicloudsdkges.v2.RegisterScenesReqScenes`]
        """
        self._scenes = scenes

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
        if not isinstance(other, RegisterScenesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
