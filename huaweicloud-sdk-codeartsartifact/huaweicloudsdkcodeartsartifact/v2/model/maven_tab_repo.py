# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MavenTabRepo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'release': 'str',
        'snapshot': 'str'
    }

    attribute_map = {
        'release': 'release',
        'snapshot': 'snapshot'
    }

    def __init__(self, release=None, snapshot=None):
        r"""MavenTabRepo

        The model defined in huaweicloud sdk

        :param release: **参数解释**： release仓库名称。  **取值范围**： 不涉及。
        :type release: str
        :param snapshot: **参数解释**： snapshot仓库名称。  **取值范围**： 不涉及。
        :type snapshot: str
        """
        
        

        self._release = None
        self._snapshot = None
        self.discriminator = None

        if release is not None:
            self.release = release
        if snapshot is not None:
            self.snapshot = snapshot

    @property
    def release(self):
        r"""Gets the release of this MavenTabRepo.

        **参数解释**： release仓库名称。  **取值范围**： 不涉及。

        :return: The release of this MavenTabRepo.
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        r"""Sets the release of this MavenTabRepo.

        **参数解释**： release仓库名称。  **取值范围**： 不涉及。

        :param release: The release of this MavenTabRepo.
        :type release: str
        """
        self._release = release

    @property
    def snapshot(self):
        r"""Gets the snapshot of this MavenTabRepo.

        **参数解释**： snapshot仓库名称。  **取值范围**： 不涉及。

        :return: The snapshot of this MavenTabRepo.
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        r"""Sets the snapshot of this MavenTabRepo.

        **参数解释**： snapshot仓库名称。  **取值范围**： 不涉及。

        :param snapshot: The snapshot of this MavenTabRepo.
        :type snapshot: str
        """
        self._snapshot = snapshot

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
        if not isinstance(other, MavenTabRepo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
