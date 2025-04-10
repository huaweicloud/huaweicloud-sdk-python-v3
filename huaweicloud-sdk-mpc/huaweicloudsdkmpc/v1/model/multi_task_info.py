# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'int',
        'error': 'ErrorResponse',
        'output_file': 'SourceInfo'
    }

    attribute_map = {
        'template_id': 'template_id',
        'error': 'error',
        'output_file': 'output_file'
    }

    def __init__(self, template_id=None, error=None, output_file=None):
        r"""MultiTaskInfo

        The model defined in huaweicloud sdk

        :param template_id: 转码模板ID。
        :type template_id: int
        :param error: 
        :type error: :class:`huaweicloudsdkmpc.v1.ErrorResponse`
        :param output_file: 
        :type output_file: :class:`huaweicloudsdkmpc.v1.SourceInfo`
        """
        
        

        self._template_id = None
        self._error = None
        self._output_file = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if error is not None:
            self.error = error
        if output_file is not None:
            self.output_file = output_file

    @property
    def template_id(self):
        r"""Gets the template_id of this MultiTaskInfo.

        转码模板ID。

        :return: The template_id of this MultiTaskInfo.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this MultiTaskInfo.

        转码模板ID。

        :param template_id: The template_id of this MultiTaskInfo.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def error(self):
        r"""Gets the error of this MultiTaskInfo.

        :return: The error of this MultiTaskInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.ErrorResponse`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this MultiTaskInfo.

        :param error: The error of this MultiTaskInfo.
        :type error: :class:`huaweicloudsdkmpc.v1.ErrorResponse`
        """
        self._error = error

    @property
    def output_file(self):
        r"""Gets the output_file of this MultiTaskInfo.

        :return: The output_file of this MultiTaskInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.SourceInfo`
        """
        return self._output_file

    @output_file.setter
    def output_file(self, output_file):
        r"""Sets the output_file of this MultiTaskInfo.

        :param output_file: The output_file of this MultiTaskInfo.
        :type output_file: :class:`huaweicloudsdkmpc.v1.SourceInfo`
        """
        self._output_file = output_file

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
        if not isinstance(other, MultiTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
