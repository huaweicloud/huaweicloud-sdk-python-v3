# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'method': 'str',
        'file': 'str',
        'output_dir': 'str'
    }

    attribute_map = {
        'method': 'method',
        'file': 'file',
        'output_dir': 'output_dir'
    }

    def __init__(self, method=None, file=None, output_dir=None):
        r"""CreateClusterJobReq

        The model defined in huaweicloud sdk

        :param method: 聚类方法,当前仅支持hiq_mc
        :type method: str
        :param file: 分子聚类源数据
        :type file: str
        :param output_dir: 分子聚类输出结果
        :type output_dir: str
        """
        
        

        self._method = None
        self._file = None
        self._output_dir = None
        self.discriminator = None

        self.method = method
        self.file = file
        self.output_dir = output_dir

    @property
    def method(self):
        r"""Gets the method of this CreateClusterJobReq.

        聚类方法,当前仅支持hiq_mc

        :return: The method of this CreateClusterJobReq.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this CreateClusterJobReq.

        聚类方法,当前仅支持hiq_mc

        :param method: The method of this CreateClusterJobReq.
        :type method: str
        """
        self._method = method

    @property
    def file(self):
        r"""Gets the file of this CreateClusterJobReq.

        分子聚类源数据

        :return: The file of this CreateClusterJobReq.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this CreateClusterJobReq.

        分子聚类源数据

        :param file: The file of this CreateClusterJobReq.
        :type file: str
        """
        self._file = file

    @property
    def output_dir(self):
        r"""Gets the output_dir of this CreateClusterJobReq.

        分子聚类输出结果

        :return: The output_dir of this CreateClusterJobReq.
        :rtype: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        r"""Sets the output_dir of this CreateClusterJobReq.

        分子聚类输出结果

        :param output_dir: The output_dir of this CreateClusterJobReq.
        :type output_dir: str
        """
        self._output_dir = output_dir

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
        if not isinstance(other, CreateClusterJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
