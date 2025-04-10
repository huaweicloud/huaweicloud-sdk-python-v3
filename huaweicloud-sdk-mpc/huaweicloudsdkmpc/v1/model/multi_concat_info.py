# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiConcatInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inputs': 'list[ObsObjInfo]',
        'trans_template_ids': 'list[int]',
        'av_parameters': 'list[AvParameters]',
        'output': 'ObsObjInfo',
        'image_watermark_settings': 'list[ImageWatermarkSetting]'
    }

    attribute_map = {
        'inputs': 'inputs',
        'trans_template_ids': 'trans_template_ids',
        'av_parameters': 'av_parameters',
        'output': 'output',
        'image_watermark_settings': 'image_watermark_settings'
    }

    def __init__(self, inputs=None, trans_template_ids=None, av_parameters=None, output=None, image_watermark_settings=None):
        r"""MultiConcatInfo

        The model defined in huaweicloud sdk

        :param inputs: 拼接任务输入源地址。
        :type inputs: list[:class:`huaweicloudsdkmpc.v1.ObsObjInfo`]
        :param trans_template_ids: 拼接完成后转码对应的转码模板ID 
        :type trans_template_ids: list[int]
        :param av_parameters: 转码参数。 设置“trans_template_id”和此参数，则优先使用此参数进行转码。 
        :type av_parameters: list[:class:`huaweicloudsdkmpc.v1.AvParameters`]
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param image_watermark_settings: 水印信息。
        :type image_watermark_settings: list[:class:`huaweicloudsdkmpc.v1.ImageWatermarkSetting`]
        """
        
        

        self._inputs = None
        self._trans_template_ids = None
        self._av_parameters = None
        self._output = None
        self._image_watermark_settings = None
        self.discriminator = None

        self.inputs = inputs
        if trans_template_ids is not None:
            self.trans_template_ids = trans_template_ids
        if av_parameters is not None:
            self.av_parameters = av_parameters
        self.output = output
        if image_watermark_settings is not None:
            self.image_watermark_settings = image_watermark_settings

    @property
    def inputs(self):
        r"""Gets the inputs of this MultiConcatInfo.

        拼接任务输入源地址。

        :return: The inputs of this MultiConcatInfo.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.ObsObjInfo`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this MultiConcatInfo.

        拼接任务输入源地址。

        :param inputs: The inputs of this MultiConcatInfo.
        :type inputs: list[:class:`huaweicloudsdkmpc.v1.ObsObjInfo`]
        """
        self._inputs = inputs

    @property
    def trans_template_ids(self):
        r"""Gets the trans_template_ids of this MultiConcatInfo.

        拼接完成后转码对应的转码模板ID 

        :return: The trans_template_ids of this MultiConcatInfo.
        :rtype: list[int]
        """
        return self._trans_template_ids

    @trans_template_ids.setter
    def trans_template_ids(self, trans_template_ids):
        r"""Sets the trans_template_ids of this MultiConcatInfo.

        拼接完成后转码对应的转码模板ID 

        :param trans_template_ids: The trans_template_ids of this MultiConcatInfo.
        :type trans_template_ids: list[int]
        """
        self._trans_template_ids = trans_template_ids

    @property
    def av_parameters(self):
        r"""Gets the av_parameters of this MultiConcatInfo.

        转码参数。 设置“trans_template_id”和此参数，则优先使用此参数进行转码。 

        :return: The av_parameters of this MultiConcatInfo.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.AvParameters`]
        """
        return self._av_parameters

    @av_parameters.setter
    def av_parameters(self, av_parameters):
        r"""Sets the av_parameters of this MultiConcatInfo.

        转码参数。 设置“trans_template_id”和此参数，则优先使用此参数进行转码。 

        :param av_parameters: The av_parameters of this MultiConcatInfo.
        :type av_parameters: list[:class:`huaweicloudsdkmpc.v1.AvParameters`]
        """
        self._av_parameters = av_parameters

    @property
    def output(self):
        r"""Gets the output of this MultiConcatInfo.

        :return: The output of this MultiConcatInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this MultiConcatInfo.

        :param output: The output of this MultiConcatInfo.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def image_watermark_settings(self):
        r"""Gets the image_watermark_settings of this MultiConcatInfo.

        水印信息。

        :return: The image_watermark_settings of this MultiConcatInfo.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.ImageWatermarkSetting`]
        """
        return self._image_watermark_settings

    @image_watermark_settings.setter
    def image_watermark_settings(self, image_watermark_settings):
        r"""Sets the image_watermark_settings of this MultiConcatInfo.

        水印信息。

        :param image_watermark_settings: The image_watermark_settings of this MultiConcatInfo.
        :type image_watermark_settings: list[:class:`huaweicloudsdkmpc.v1.ImageWatermarkSetting`]
        """
        self._image_watermark_settings = image_watermark_settings

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
        if not isinstance(other, MultiConcatInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
