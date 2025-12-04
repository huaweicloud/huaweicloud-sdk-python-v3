# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigFeatures:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'feature_id': 'str',
        'status': 'int',
        'description': 'str'
    }

    attribute_map = {
        'feature_id': 'featureId',
        'status': 'status',
        'description': 'description'
    }

    def __init__(self, feature_id=None, status=None, description=None):
        r"""ListConfigFeatures

        The model defined in huaweicloud sdk

        :param feature_id: **参数解释**： 特性ID。     **取值范围**： 不涉及。
        :type feature_id: str
        :param status: **参数解释**： 状态。  **取值范围**： - 0：特性关闭。 - 1：特性开启。
        :type status: int
        :param description: **参数解释**： 特性描述。  **取值范围**： 不涉及。
        :type description: str
        """
        
        

        self._feature_id = None
        self._status = None
        self._description = None
        self.discriminator = None

        if feature_id is not None:
            self.feature_id = feature_id
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description

    @property
    def feature_id(self):
        r"""Gets the feature_id of this ListConfigFeatures.

        **参数解释**： 特性ID。     **取值范围**： 不涉及。

        :return: The feature_id of this ListConfigFeatures.
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        r"""Sets the feature_id of this ListConfigFeatures.

        **参数解释**： 特性ID。     **取值范围**： 不涉及。

        :param feature_id: The feature_id of this ListConfigFeatures.
        :type feature_id: str
        """
        self._feature_id = feature_id

    @property
    def status(self):
        r"""Gets the status of this ListConfigFeatures.

        **参数解释**： 状态。  **取值范围**： - 0：特性关闭。 - 1：特性开启。

        :return: The status of this ListConfigFeatures.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListConfigFeatures.

        **参数解释**： 状态。  **取值范围**： - 0：特性关闭。 - 1：特性开启。

        :param status: The status of this ListConfigFeatures.
        :type status: int
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this ListConfigFeatures.

        **参数解释**： 特性描述。  **取值范围**： 不涉及。

        :return: The description of this ListConfigFeatures.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListConfigFeatures.

        **参数解释**： 特性描述。  **取值范围**： 不涉及。

        :param description: The description of this ListConfigFeatures.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ListConfigFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
