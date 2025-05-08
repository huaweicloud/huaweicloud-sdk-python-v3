# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetDocumentAtomicInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'atomic_unique_key': 'str',
        'atomic_name_zh': 'str',
        'atomic_name_en': 'str',
        'tags': 'list[str]',
        'inputs': 'list[AtomicInputModel]',
        'outputs': 'AtomicOutputModel'
    }

    attribute_map = {
        'atomic_unique_key': 'atomic_unique_key',
        'atomic_name_zh': 'atomic_name_zh',
        'atomic_name_en': 'atomic_name_en',
        'tags': 'tags',
        'inputs': 'inputs',
        'outputs': 'outputs'
    }

    def __init__(self, atomic_unique_key=None, atomic_name_zh=None, atomic_name_en=None, tags=None, inputs=None, outputs=None):
        r"""GetDocumentAtomicInfoResponse

        The model defined in huaweicloud sdk

        :param atomic_unique_key: 原子能力唯一标识：只允许字母+下划线，字母开头
        :type atomic_unique_key: str
        :param atomic_name_zh: 中文名
        :type atomic_name_zh: str
        :param atomic_name_en: 英文名
        :type atomic_name_en: str
        :param tags: 标签信息
        :type tags: list[str]
        :param inputs: 原子能力入参
        :type inputs: list[:class:`huaweicloudsdkcoc.v1.AtomicInputModel`]
        :param outputs: 
        :type outputs: :class:`huaweicloudsdkcoc.v1.AtomicOutputModel`
        """
        
        super(GetDocumentAtomicInfoResponse, self).__init__()

        self._atomic_unique_key = None
        self._atomic_name_zh = None
        self._atomic_name_en = None
        self._tags = None
        self._inputs = None
        self._outputs = None
        self.discriminator = None

        if atomic_unique_key is not None:
            self.atomic_unique_key = atomic_unique_key
        if atomic_name_zh is not None:
            self.atomic_name_zh = atomic_name_zh
        if atomic_name_en is not None:
            self.atomic_name_en = atomic_name_en
        if tags is not None:
            self.tags = tags
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs

    @property
    def atomic_unique_key(self):
        r"""Gets the atomic_unique_key of this GetDocumentAtomicInfoResponse.

        原子能力唯一标识：只允许字母+下划线，字母开头

        :return: The atomic_unique_key of this GetDocumentAtomicInfoResponse.
        :rtype: str
        """
        return self._atomic_unique_key

    @atomic_unique_key.setter
    def atomic_unique_key(self, atomic_unique_key):
        r"""Sets the atomic_unique_key of this GetDocumentAtomicInfoResponse.

        原子能力唯一标识：只允许字母+下划线，字母开头

        :param atomic_unique_key: The atomic_unique_key of this GetDocumentAtomicInfoResponse.
        :type atomic_unique_key: str
        """
        self._atomic_unique_key = atomic_unique_key

    @property
    def atomic_name_zh(self):
        r"""Gets the atomic_name_zh of this GetDocumentAtomicInfoResponse.

        中文名

        :return: The atomic_name_zh of this GetDocumentAtomicInfoResponse.
        :rtype: str
        """
        return self._atomic_name_zh

    @atomic_name_zh.setter
    def atomic_name_zh(self, atomic_name_zh):
        r"""Sets the atomic_name_zh of this GetDocumentAtomicInfoResponse.

        中文名

        :param atomic_name_zh: The atomic_name_zh of this GetDocumentAtomicInfoResponse.
        :type atomic_name_zh: str
        """
        self._atomic_name_zh = atomic_name_zh

    @property
    def atomic_name_en(self):
        r"""Gets the atomic_name_en of this GetDocumentAtomicInfoResponse.

        英文名

        :return: The atomic_name_en of this GetDocumentAtomicInfoResponse.
        :rtype: str
        """
        return self._atomic_name_en

    @atomic_name_en.setter
    def atomic_name_en(self, atomic_name_en):
        r"""Sets the atomic_name_en of this GetDocumentAtomicInfoResponse.

        英文名

        :param atomic_name_en: The atomic_name_en of this GetDocumentAtomicInfoResponse.
        :type atomic_name_en: str
        """
        self._atomic_name_en = atomic_name_en

    @property
    def tags(self):
        r"""Gets the tags of this GetDocumentAtomicInfoResponse.

        标签信息

        :return: The tags of this GetDocumentAtomicInfoResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this GetDocumentAtomicInfoResponse.

        标签信息

        :param tags: The tags of this GetDocumentAtomicInfoResponse.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def inputs(self):
        r"""Gets the inputs of this GetDocumentAtomicInfoResponse.

        原子能力入参

        :return: The inputs of this GetDocumentAtomicInfoResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.AtomicInputModel`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this GetDocumentAtomicInfoResponse.

        原子能力入参

        :param inputs: The inputs of this GetDocumentAtomicInfoResponse.
        :type inputs: list[:class:`huaweicloudsdkcoc.v1.AtomicInputModel`]
        """
        self._inputs = inputs

    @property
    def outputs(self):
        r"""Gets the outputs of this GetDocumentAtomicInfoResponse.

        :return: The outputs of this GetDocumentAtomicInfoResponse.
        :rtype: :class:`huaweicloudsdkcoc.v1.AtomicOutputModel`
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this GetDocumentAtomicInfoResponse.

        :param outputs: The outputs of this GetDocumentAtomicInfoResponse.
        :type outputs: :class:`huaweicloudsdkcoc.v1.AtomicOutputModel`
        """
        self._outputs = outputs

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
        if not isinstance(other, GetDocumentAtomicInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
