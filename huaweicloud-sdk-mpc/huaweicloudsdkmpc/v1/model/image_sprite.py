# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageSprite:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'params': 'ImageSpritePara',
        'output': 'ObsObjInfo',
        'output_object_name': 'str',
        'webvtt_object_name': 'str'
    }

    attribute_map = {
        'params': 'params',
        'output': 'output',
        'output_object_name': 'output_object_name',
        'webvtt_object_name': 'webvtt_object_name'
    }

    def __init__(self, params=None, output=None, output_object_name=None, webvtt_object_name=None):
        r"""ImageSprite

        The model defined in huaweicloud sdk

        :param params: 
        :type params: :class:`huaweicloudsdkmpc.v1.ImageSpritePara`
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output_object_name: 截取雪碧图后，雪碧图图片文件的输出文件名，如果不填，则默认为：{inputName}_imageSprite_{雪碧图id}_{number}.{format}.{雪碧图id}和{number}从0开始递增 
        :type output_object_name: str
        :param webvtt_object_name: 截取雪碧图后，Web VTT 文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：{inputName}_imageSprite_{雪碧图_id}.vtt 
        :type webvtt_object_name: str
        """
        
        

        self._params = None
        self._output = None
        self._output_object_name = None
        self._webvtt_object_name = None
        self.discriminator = None

        self.params = params
        if output is not None:
            self.output = output
        if output_object_name is not None:
            self.output_object_name = output_object_name
        if webvtt_object_name is not None:
            self.webvtt_object_name = webvtt_object_name

    @property
    def params(self):
        r"""Gets the params of this ImageSprite.

        :return: The params of this ImageSprite.
        :rtype: :class:`huaweicloudsdkmpc.v1.ImageSpritePara`
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this ImageSprite.

        :param params: The params of this ImageSprite.
        :type params: :class:`huaweicloudsdkmpc.v1.ImageSpritePara`
        """
        self._params = params

    @property
    def output(self):
        r"""Gets the output of this ImageSprite.

        :return: The output of this ImageSprite.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ImageSprite.

        :param output: The output of this ImageSprite.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def output_object_name(self):
        r"""Gets the output_object_name of this ImageSprite.

        截取雪碧图后，雪碧图图片文件的输出文件名，如果不填，则默认为：{inputName}_imageSprite_{雪碧图id}_{number}.{format}.{雪碧图id}和{number}从0开始递增 

        :return: The output_object_name of this ImageSprite.
        :rtype: str
        """
        return self._output_object_name

    @output_object_name.setter
    def output_object_name(self, output_object_name):
        r"""Sets the output_object_name of this ImageSprite.

        截取雪碧图后，雪碧图图片文件的输出文件名，如果不填，则默认为：{inputName}_imageSprite_{雪碧图id}_{number}.{format}.{雪碧图id}和{number}从0开始递增 

        :param output_object_name: The output_object_name of this ImageSprite.
        :type output_object_name: str
        """
        self._output_object_name = output_object_name

    @property
    def webvtt_object_name(self):
        r"""Gets the webvtt_object_name of this ImageSprite.

        截取雪碧图后，Web VTT 文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：{inputName}_imageSprite_{雪碧图_id}.vtt 

        :return: The webvtt_object_name of this ImageSprite.
        :rtype: str
        """
        return self._webvtt_object_name

    @webvtt_object_name.setter
    def webvtt_object_name(self, webvtt_object_name):
        r"""Sets the webvtt_object_name of this ImageSprite.

        截取雪碧图后，Web VTT 文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：{inputName}_imageSprite_{雪碧图_id}.vtt 

        :param webvtt_object_name: The webvtt_object_name of this ImageSprite.
        :type webvtt_object_name: str
        """
        self._webvtt_object_name = webvtt_object_name

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
        if not isinstance(other, ImageSprite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
