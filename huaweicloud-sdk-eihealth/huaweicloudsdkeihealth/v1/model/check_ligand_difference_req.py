# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckLigandDifferenceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'method': 'CheckLigandDifferenceMethod',
        'file': 'DrugFile',
        'ref_file': 'DrugFile'
    }

    attribute_map = {
        'method': 'method',
        'file': 'file',
        'ref_file': 'ref_file'
    }

    def __init__(self, method=None, file=None, ref_file=None):
        """CheckLigandDifferenceReq

        The model defined in huaweicloud sdk

        :param method: 
        :type method: :class:`huaweicloudsdkeihealth.v1.CheckLigandDifferenceMethod`
        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        :param ref_file: 
        :type ref_file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        
        

        self._method = None
        self._file = None
        self._ref_file = None
        self.discriminator = None

        self.method = method
        self.file = file
        self.ref_file = ref_file

    @property
    def method(self):
        """Gets the method of this CheckLigandDifferenceReq.

        :return: The method of this CheckLigandDifferenceReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.CheckLigandDifferenceMethod`
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this CheckLigandDifferenceReq.

        :param method: The method of this CheckLigandDifferenceReq.
        :type method: :class:`huaweicloudsdkeihealth.v1.CheckLigandDifferenceMethod`
        """
        self._method = method

    @property
    def file(self):
        """Gets the file of this CheckLigandDifferenceReq.

        :return: The file of this CheckLigandDifferenceReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this CheckLigandDifferenceReq.

        :param file: The file of this CheckLigandDifferenceReq.
        :type file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        self._file = file

    @property
    def ref_file(self):
        """Gets the ref_file of this CheckLigandDifferenceReq.

        :return: The ref_file of this CheckLigandDifferenceReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        return self._ref_file

    @ref_file.setter
    def ref_file(self, ref_file):
        """Sets the ref_file of this CheckLigandDifferenceReq.

        :param ref_file: The ref_file of this CheckLigandDifferenceReq.
        :type ref_file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        self._ref_file = ref_file

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
        if not isinstance(other, CheckLigandDifferenceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
