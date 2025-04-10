# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunFormatConverterReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'ConvertFile',
        'in_format': 'str',
        'out_format': 'str'
    }

    attribute_map = {
        'file': 'file',
        'in_format': 'in_format',
        'out_format': 'out_format'
    }

    def __init__(self, file=None, in_format=None, out_format=None):
        r"""RunFormatConverterReq

        The model defined in huaweicloud sdk

        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.ConvertFile`
        :param in_format: 待转换文件格式，支持PDB、SDF、MOL2、SMI。
        :type in_format: str
        :param out_format: 转换后文件格式，支持PDB、SDF、MOL2、SMI。
        :type out_format: str
        """
        
        

        self._file = None
        self._in_format = None
        self._out_format = None
        self.discriminator = None

        self.file = file
        self.in_format = in_format
        self.out_format = out_format

    @property
    def file(self):
        r"""Gets the file of this RunFormatConverterReq.

        :return: The file of this RunFormatConverterReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ConvertFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this RunFormatConverterReq.

        :param file: The file of this RunFormatConverterReq.
        :type file: :class:`huaweicloudsdkeihealth.v1.ConvertFile`
        """
        self._file = file

    @property
    def in_format(self):
        r"""Gets the in_format of this RunFormatConverterReq.

        待转换文件格式，支持PDB、SDF、MOL2、SMI。

        :return: The in_format of this RunFormatConverterReq.
        :rtype: str
        """
        return self._in_format

    @in_format.setter
    def in_format(self, in_format):
        r"""Sets the in_format of this RunFormatConverterReq.

        待转换文件格式，支持PDB、SDF、MOL2、SMI。

        :param in_format: The in_format of this RunFormatConverterReq.
        :type in_format: str
        """
        self._in_format = in_format

    @property
    def out_format(self):
        r"""Gets the out_format of this RunFormatConverterReq.

        转换后文件格式，支持PDB、SDF、MOL2、SMI。

        :return: The out_format of this RunFormatConverterReq.
        :rtype: str
        """
        return self._out_format

    @out_format.setter
    def out_format(self, out_format):
        r"""Sets the out_format of this RunFormatConverterReq.

        转换后文件格式，支持PDB、SDF、MOL2、SMI。

        :param out_format: The out_format of this RunFormatConverterReq.
        :type out_format: str
        """
        self._out_format = out_format

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
        if not isinstance(other, RunFormatConverterReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
