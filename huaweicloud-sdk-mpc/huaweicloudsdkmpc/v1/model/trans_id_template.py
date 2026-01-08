# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransIdTemplate:

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
        'output': 'ObsObjInfo',
        'output_filename': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'output': 'output',
        'output_filename': 'output_filename'
    }

    def __init__(self, template_id=None, output=None, output_filename=None):
        r"""TransIdTemplate

        The model defined in huaweicloud sdk

        :param template_id: 输出视频对应的模板ID 
        :type template_id: int
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output_filename: 输出文件名 
        :type output_filename: str
        """
        
        

        self._template_id = None
        self._output = None
        self._output_filename = None
        self.discriminator = None

        self.template_id = template_id
        if output is not None:
            self.output = output
        if output_filename is not None:
            self.output_filename = output_filename

    @property
    def template_id(self):
        r"""Gets the template_id of this TransIdTemplate.

        输出视频对应的模板ID 

        :return: The template_id of this TransIdTemplate.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this TransIdTemplate.

        输出视频对应的模板ID 

        :param template_id: The template_id of this TransIdTemplate.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def output(self):
        r"""Gets the output of this TransIdTemplate.

        :return: The output of this TransIdTemplate.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this TransIdTemplate.

        :param output: The output of this TransIdTemplate.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def output_filename(self):
        r"""Gets the output_filename of this TransIdTemplate.

        输出文件名 

        :return: The output_filename of this TransIdTemplate.
        :rtype: str
        """
        return self._output_filename

    @output_filename.setter
    def output_filename(self, output_filename):
        r"""Sets the output_filename of this TransIdTemplate.

        输出文件名 

        :param output_filename: The output_filename of this TransIdTemplate.
        :type output_filename: str
        """
        self._output_filename = output_filename

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
        if not isinstance(other, TransIdTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
