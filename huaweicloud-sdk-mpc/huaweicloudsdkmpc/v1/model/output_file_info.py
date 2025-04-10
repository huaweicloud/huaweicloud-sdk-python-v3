# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputFileInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'output_file_name': 'str',
        'exec_description': 'str',
        'meta_data': 'SourceInfo'
    }

    attribute_map = {
        'output_file_name': 'output_file_name',
        'exec_description': 'exec_description',
        'meta_data': 'meta_data'
    }

    def __init__(self, output_file_name=None, exec_description=None, meta_data=None):
        r"""OutputFileInfo

        The model defined in huaweicloud sdk

        :param output_file_name: 输出文件名。 
        :type output_file_name: str
        :param exec_description: 处理信息。 
        :type exec_description: str
        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkmpc.v1.SourceInfo`
        """
        
        

        self._output_file_name = None
        self._exec_description = None
        self._meta_data = None
        self.discriminator = None

        if output_file_name is not None:
            self.output_file_name = output_file_name
        if exec_description is not None:
            self.exec_description = exec_description
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def output_file_name(self):
        r"""Gets the output_file_name of this OutputFileInfo.

        输出文件名。 

        :return: The output_file_name of this OutputFileInfo.
        :rtype: str
        """
        return self._output_file_name

    @output_file_name.setter
    def output_file_name(self, output_file_name):
        r"""Sets the output_file_name of this OutputFileInfo.

        输出文件名。 

        :param output_file_name: The output_file_name of this OutputFileInfo.
        :type output_file_name: str
        """
        self._output_file_name = output_file_name

    @property
    def exec_description(self):
        r"""Gets the exec_description of this OutputFileInfo.

        处理信息。 

        :return: The exec_description of this OutputFileInfo.
        :rtype: str
        """
        return self._exec_description

    @exec_description.setter
    def exec_description(self, exec_description):
        r"""Sets the exec_description of this OutputFileInfo.

        处理信息。 

        :param exec_description: The exec_description of this OutputFileInfo.
        :type exec_description: str
        """
        self._exec_description = exec_description

    @property
    def meta_data(self):
        r"""Gets the meta_data of this OutputFileInfo.

        :return: The meta_data of this OutputFileInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.SourceInfo`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        r"""Sets the meta_data of this OutputFileInfo.

        :param meta_data: The meta_data of this OutputFileInfo.
        :type meta_data: :class:`huaweicloudsdkmpc.v1.SourceInfo`
        """
        self._meta_data = meta_data

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
        if not isinstance(other, OutputFileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
