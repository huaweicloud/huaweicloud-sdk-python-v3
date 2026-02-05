# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteBackupSelectionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'selection': 'bool'
    }

    attribute_map = {
        'selection': 'selection'
    }

    def __init__(self, selection=None):
        r"""DeleteBackupSelectionRequestBody

        The model defined in huaweicloud sdk

        :param selection: 选择是否保留自动备份标志
        :type selection: bool
        """
        
        

        self._selection = None
        self.discriminator = None

        self.selection = selection

    @property
    def selection(self):
        r"""Gets the selection of this DeleteBackupSelectionRequestBody.

        选择是否保留自动备份标志

        :return: The selection of this DeleteBackupSelectionRequestBody.
        :rtype: bool
        """
        return self._selection

    @selection.setter
    def selection(self, selection):
        r"""Sets the selection of this DeleteBackupSelectionRequestBody.

        选择是否保留自动备份标志

        :param selection: The selection of this DeleteBackupSelectionRequestBody.
        :type selection: bool
        """
        self._selection = selection

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
        if not isinstance(other, DeleteBackupSelectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
