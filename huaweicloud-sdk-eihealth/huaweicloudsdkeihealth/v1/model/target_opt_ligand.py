# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetOptLigand:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'ProbeDrugFile',
        'force_field': 'str'
    }

    attribute_map = {
        'file': 'file',
        'force_field': 'force_field'
    }

    def __init__(self, file=None, force_field=None):
        r"""TargetOptLigand

        The model defined in huaweicloud sdk

        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.ProbeDrugFile`
        :param force_field: 配体力场, 支持选择gaff, gaff2
        :type force_field: str
        """
        
        

        self._file = None
        self._force_field = None
        self.discriminator = None

        self.file = file
        if force_field is not None:
            self.force_field = force_field

    @property
    def file(self):
        r"""Gets the file of this TargetOptLigand.

        :return: The file of this TargetOptLigand.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ProbeDrugFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this TargetOptLigand.

        :param file: The file of this TargetOptLigand.
        :type file: :class:`huaweicloudsdkeihealth.v1.ProbeDrugFile`
        """
        self._file = file

    @property
    def force_field(self):
        r"""Gets the force_field of this TargetOptLigand.

        配体力场, 支持选择gaff, gaff2

        :return: The force_field of this TargetOptLigand.
        :rtype: str
        """
        return self._force_field

    @force_field.setter
    def force_field(self, force_field):
        r"""Sets the force_field of this TargetOptLigand.

        配体力场, 支持选择gaff, gaff2

        :param force_field: The force_field of this TargetOptLigand.
        :type force_field: str
        """
        self._force_field = force_field

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
        if not isinstance(other, TargetOptLigand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
