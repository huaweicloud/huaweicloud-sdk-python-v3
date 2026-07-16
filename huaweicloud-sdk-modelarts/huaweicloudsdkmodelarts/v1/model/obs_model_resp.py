# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsModelResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_path': 'str',
        'local_path': 'str'
    }

    attribute_map = {
        'obs_path': 'obs_path',
        'local_path': 'local_path'
    }

    def __init__(self, obs_path=None, local_path=None):
        r"""ObsModelResp

        The model defined in huaweicloud sdk

        :param obs_path: **参数解释**：自定义训练作业产物保存的OBS地址，如：“obs://example/path”。 **取值范围**：不涉及。
        :type obs_path: str
        :param local_path: **参数解释**：自定义训练作业产物保存的宿主机的路径，如：“/example/path”。 **取值范围**：不涉及。
        :type local_path: str
        """
        
        

        self._obs_path = None
        self._local_path = None
        self.discriminator = None

        self.obs_path = obs_path
        if local_path is not None:
            self.local_path = local_path

    @property
    def obs_path(self):
        r"""Gets the obs_path of this ObsModelResp.

        **参数解释**：自定义训练作业产物保存的OBS地址，如：“obs://example/path”。 **取值范围**：不涉及。

        :return: The obs_path of this ObsModelResp.
        :rtype: str
        """
        return self._obs_path

    @obs_path.setter
    def obs_path(self, obs_path):
        r"""Sets the obs_path of this ObsModelResp.

        **参数解释**：自定义训练作业产物保存的OBS地址，如：“obs://example/path”。 **取值范围**：不涉及。

        :param obs_path: The obs_path of this ObsModelResp.
        :type obs_path: str
        """
        self._obs_path = obs_path

    @property
    def local_path(self):
        r"""Gets the local_path of this ObsModelResp.

        **参数解释**：自定义训练作业产物保存的宿主机的路径，如：“/example/path”。 **取值范围**：不涉及。

        :return: The local_path of this ObsModelResp.
        :rtype: str
        """
        return self._local_path

    @local_path.setter
    def local_path(self, local_path):
        r"""Sets the local_path of this ObsModelResp.

        **参数解释**：自定义训练作业产物保存的宿主机的路径，如：“/example/path”。 **取值范围**：不涉及。

        :param local_path: The local_path of this ObsModelResp.
        :type local_path: str
        """
        self._local_path = local_path

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ObsModelResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
