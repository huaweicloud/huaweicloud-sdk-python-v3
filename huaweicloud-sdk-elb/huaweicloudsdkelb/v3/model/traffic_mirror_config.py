# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrafficMirrorConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_ids': 'list[str]',
        'mirror_request_body_enable': 'bool'
    }

    attribute_map = {
        'target_ids': 'target_ids',
        'mirror_request_body_enable': 'mirror_request_body_enable'
    }

    def __init__(self, target_ids=None, mirror_request_body_enable=None):
        r"""TrafficMirrorConfig

        The model defined in huaweicloud sdk

        :param target_ids: **参数解释**：流量镜像的目的后端服务器组ID。  **取值范围**：不涉及
        :type target_ids: list[str]
        :param mirror_request_body_enable: **参数解释**：镜像请求是否携带请求体，默认true。  **取值范围**：不涉及
        :type mirror_request_body_enable: bool
        """
        
        

        self._target_ids = None
        self._mirror_request_body_enable = None
        self.discriminator = None

        if target_ids is not None:
            self.target_ids = target_ids
        if mirror_request_body_enable is not None:
            self.mirror_request_body_enable = mirror_request_body_enable

    @property
    def target_ids(self):
        r"""Gets the target_ids of this TrafficMirrorConfig.

        **参数解释**：流量镜像的目的后端服务器组ID。  **取值范围**：不涉及

        :return: The target_ids of this TrafficMirrorConfig.
        :rtype: list[str]
        """
        return self._target_ids

    @target_ids.setter
    def target_ids(self, target_ids):
        r"""Sets the target_ids of this TrafficMirrorConfig.

        **参数解释**：流量镜像的目的后端服务器组ID。  **取值范围**：不涉及

        :param target_ids: The target_ids of this TrafficMirrorConfig.
        :type target_ids: list[str]
        """
        self._target_ids = target_ids

    @property
    def mirror_request_body_enable(self):
        r"""Gets the mirror_request_body_enable of this TrafficMirrorConfig.

        **参数解释**：镜像请求是否携带请求体，默认true。  **取值范围**：不涉及

        :return: The mirror_request_body_enable of this TrafficMirrorConfig.
        :rtype: bool
        """
        return self._mirror_request_body_enable

    @mirror_request_body_enable.setter
    def mirror_request_body_enable(self, mirror_request_body_enable):
        r"""Sets the mirror_request_body_enable of this TrafficMirrorConfig.

        **参数解释**：镜像请求是否携带请求体，默认true。  **取值范围**：不涉及

        :param mirror_request_body_enable: The mirror_request_body_enable of this TrafficMirrorConfig.
        :type mirror_request_body_enable: bool
        """
        self._mirror_request_body_enable = mirror_request_body_enable

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
        if not isinstance(other, TrafficMirrorConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
