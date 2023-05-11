# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MbTaskParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status_description': 'str',
        'output_filename': 'str',
        'metadata': 'MetaData'
    }

    attribute_map = {
        'status_description': 'status_description',
        'output_filename': 'output_filename',
        'metadata': 'metadata'
    }

    def __init__(self, status_description=None, output_filename=None, metadata=None):
        """MbTaskParameter

        The model defined in huaweicloud sdk

        :param status_description: 具体状态描述，FAILED时可用于分析问题。 
        :type status_description: str
        :param output_filename: 输出文件名称。 
        :type output_filename: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmpc.v1.MetaData`
        """
        
        

        self._status_description = None
        self._output_filename = None
        self._metadata = None
        self.discriminator = None

        if status_description is not None:
            self.status_description = status_description
        if output_filename is not None:
            self.output_filename = output_filename
        if metadata is not None:
            self.metadata = metadata

    @property
    def status_description(self):
        """Gets the status_description of this MbTaskParameter.

        具体状态描述，FAILED时可用于分析问题。 

        :return: The status_description of this MbTaskParameter.
        :rtype: str
        """
        return self._status_description

    @status_description.setter
    def status_description(self, status_description):
        """Sets the status_description of this MbTaskParameter.

        具体状态描述，FAILED时可用于分析问题。 

        :param status_description: The status_description of this MbTaskParameter.
        :type status_description: str
        """
        self._status_description = status_description

    @property
    def output_filename(self):
        """Gets the output_filename of this MbTaskParameter.

        输出文件名称。 

        :return: The output_filename of this MbTaskParameter.
        :rtype: str
        """
        return self._output_filename

    @output_filename.setter
    def output_filename(self, output_filename):
        """Sets the output_filename of this MbTaskParameter.

        输出文件名称。 

        :param output_filename: The output_filename of this MbTaskParameter.
        :type output_filename: str
        """
        self._output_filename = output_filename

    @property
    def metadata(self):
        """Gets the metadata of this MbTaskParameter.

        :return: The metadata of this MbTaskParameter.
        :rtype: :class:`huaweicloudsdkmpc.v1.MetaData`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this MbTaskParameter.

        :param metadata: The metadata of this MbTaskParameter.
        :type metadata: :class:`huaweicloudsdkmpc.v1.MetaData`
        """
        self._metadata = metadata

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
        if not isinstance(other, MbTaskParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
