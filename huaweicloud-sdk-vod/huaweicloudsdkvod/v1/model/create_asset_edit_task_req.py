# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAssetEditTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inputs': 'list[EditInput]',
        'editing_settings': 'VodEditingSetting'
    }

    attribute_map = {
        'inputs': 'inputs',
        'editing_settings': 'editing_settings'
    }

    def __init__(self, inputs=None, editing_settings=None):
        r"""CreateAssetEditTaskReq

        The model defined in huaweicloud sdk

        :param inputs: 待编辑媒资列表，最多支持20个。 
        :type inputs: list[:class:`huaweicloudsdkvod.v1.EditInput`]
        :param editing_settings: 
        :type editing_settings: :class:`huaweicloudsdkvod.v1.VodEditingSetting`
        """
        
        

        self._inputs = None
        self._editing_settings = None
        self.discriminator = None

        self.inputs = inputs
        if editing_settings is not None:
            self.editing_settings = editing_settings

    @property
    def inputs(self):
        r"""Gets the inputs of this CreateAssetEditTaskReq.

        待编辑媒资列表，最多支持20个。 

        :return: The inputs of this CreateAssetEditTaskReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.EditInput`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this CreateAssetEditTaskReq.

        待编辑媒资列表，最多支持20个。 

        :param inputs: The inputs of this CreateAssetEditTaskReq.
        :type inputs: list[:class:`huaweicloudsdkvod.v1.EditInput`]
        """
        self._inputs = inputs

    @property
    def editing_settings(self):
        r"""Gets the editing_settings of this CreateAssetEditTaskReq.

        :return: The editing_settings of this CreateAssetEditTaskReq.
        :rtype: :class:`huaweicloudsdkvod.v1.VodEditingSetting`
        """
        return self._editing_settings

    @editing_settings.setter
    def editing_settings(self, editing_settings):
        r"""Sets the editing_settings of this CreateAssetEditTaskReq.

        :param editing_settings: The editing_settings of this CreateAssetEditTaskReq.
        :type editing_settings: :class:`huaweicloudsdkvod.v1.VodEditingSetting`
        """
        self._editing_settings = editing_settings

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
        if not isinstance(other, CreateAssetEditTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
