# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AffinityResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'affinity_type': 'str',
        'required': 'bool',
        'selection_mode': 'str',
        'targets': 'dict(str, str)'
    }

    attribute_map = {
        'affinity_type': 'affinity_type',
        'required': 'required',
        'selection_mode': 'selection_mode',
        'targets': 'targets'
    }

    def __init__(self, affinity_type=None, required=None, selection_mode=None, targets=None):
        r"""AffinityResponse

        The model defined in huaweicloud sdk

        :param affinity_type: **参数解释：** 节点亲和类型。 **取值范围：** - AFFINITY：亲和。 - ANTI_AFFINITY：反亲和。
        :type affinity_type: str
        :param required: **参数解释：** 是否设置强亲和。 **取值范围：** - true：设置强亲和。 - false：不设置强亲和。
        :type required: bool
        :param selection_mode: **参数解释：** 选择节点方式。 **取值范围：** IP。
        :type selection_mode: str
        :param targets: **参数解释：** 通过上述方式选择的列表，长度不能超过20。
        :type targets: dict(str, str)
        """
        
        

        self._affinity_type = None
        self._required = None
        self._selection_mode = None
        self._targets = None
        self.discriminator = None

        self.affinity_type = affinity_type
        self.required = required
        self.selection_mode = selection_mode
        self.targets = targets

    @property
    def affinity_type(self):
        r"""Gets the affinity_type of this AffinityResponse.

        **参数解释：** 节点亲和类型。 **取值范围：** - AFFINITY：亲和。 - ANTI_AFFINITY：反亲和。

        :return: The affinity_type of this AffinityResponse.
        :rtype: str
        """
        return self._affinity_type

    @affinity_type.setter
    def affinity_type(self, affinity_type):
        r"""Sets the affinity_type of this AffinityResponse.

        **参数解释：** 节点亲和类型。 **取值范围：** - AFFINITY：亲和。 - ANTI_AFFINITY：反亲和。

        :param affinity_type: The affinity_type of this AffinityResponse.
        :type affinity_type: str
        """
        self._affinity_type = affinity_type

    @property
    def required(self):
        r"""Gets the required of this AffinityResponse.

        **参数解释：** 是否设置强亲和。 **取值范围：** - true：设置强亲和。 - false：不设置强亲和。

        :return: The required of this AffinityResponse.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this AffinityResponse.

        **参数解释：** 是否设置强亲和。 **取值范围：** - true：设置强亲和。 - false：不设置强亲和。

        :param required: The required of this AffinityResponse.
        :type required: bool
        """
        self._required = required

    @property
    def selection_mode(self):
        r"""Gets the selection_mode of this AffinityResponse.

        **参数解释：** 选择节点方式。 **取值范围：** IP。

        :return: The selection_mode of this AffinityResponse.
        :rtype: str
        """
        return self._selection_mode

    @selection_mode.setter
    def selection_mode(self, selection_mode):
        r"""Sets the selection_mode of this AffinityResponse.

        **参数解释：** 选择节点方式。 **取值范围：** IP。

        :param selection_mode: The selection_mode of this AffinityResponse.
        :type selection_mode: str
        """
        self._selection_mode = selection_mode

    @property
    def targets(self):
        r"""Gets the targets of this AffinityResponse.

        **参数解释：** 通过上述方式选择的列表，长度不能超过20。

        :return: The targets of this AffinityResponse.
        :rtype: dict(str, str)
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this AffinityResponse.

        **参数解释：** 通过上述方式选择的列表，长度不能超过20。

        :param targets: The targets of this AffinityResponse.
        :type targets: dict(str, str)
        """
        self._targets = targets

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
        if not isinstance(other, AffinityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
