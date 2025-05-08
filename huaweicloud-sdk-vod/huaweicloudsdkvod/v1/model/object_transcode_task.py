# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectTranscodeTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trans_template_id': 'str',
        'output_name': 'str',
        'output': 'ObsInfo'
    }

    attribute_map = {
        'trans_template_id': 'trans_template_id',
        'output_name': 'output_name',
        'output': 'output'
    }

    def __init__(self, trans_template_id=None, output_name=None, output=None):
        r"""ObjectTranscodeTask

        The model defined in huaweicloud sdk

        :param trans_template_id: 转码模板ID 
        :type trans_template_id: str
        :param output_name: 转码输出文件名 
        :type output_name: str
        :param output: 
        :type output: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        
        

        self._trans_template_id = None
        self._output_name = None
        self._output = None
        self.discriminator = None

        self.trans_template_id = trans_template_id
        if output_name is not None:
            self.output_name = output_name
        if output is not None:
            self.output = output

    @property
    def trans_template_id(self):
        r"""Gets the trans_template_id of this ObjectTranscodeTask.

        转码模板ID 

        :return: The trans_template_id of this ObjectTranscodeTask.
        :rtype: str
        """
        return self._trans_template_id

    @trans_template_id.setter
    def trans_template_id(self, trans_template_id):
        r"""Sets the trans_template_id of this ObjectTranscodeTask.

        转码模板ID 

        :param trans_template_id: The trans_template_id of this ObjectTranscodeTask.
        :type trans_template_id: str
        """
        self._trans_template_id = trans_template_id

    @property
    def output_name(self):
        r"""Gets the output_name of this ObjectTranscodeTask.

        转码输出文件名 

        :return: The output_name of this ObjectTranscodeTask.
        :rtype: str
        """
        return self._output_name

    @output_name.setter
    def output_name(self, output_name):
        r"""Sets the output_name of this ObjectTranscodeTask.

        转码输出文件名 

        :param output_name: The output_name of this ObjectTranscodeTask.
        :type output_name: str
        """
        self._output_name = output_name

    @property
    def output(self):
        r"""Gets the output of this ObjectTranscodeTask.

        :return: The output of this ObjectTranscodeTask.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ObjectTranscodeTask.

        :param output: The output of this ObjectTranscodeTask.
        :type output: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._output = output

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
        if not isinstance(other, ObjectTranscodeTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
