# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateModelReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'type': 'ModelType',
        'file': 'ModelFile',
        'shareable': 'bool',
        'base_model_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'file': 'file',
        'shareable': 'shareable',
        'base_model_id': 'base_model_id'
    }

    def __init__(self, name=None, description=None, type=None, file=None, shareable=None, base_model_id=None):
        r"""CreateModelReq

        The model defined in huaweicloud sdk

        :param name: 模型名称，取值范围：[5,32]，允许大小写字母、数字、下划线(_)、中划线(-)和空格,只能以字母开头
        :type name: str
        :param description: 模型描述信息
        :type description: str
        :param type: 
        :type type: :class:`huaweicloudsdkeihealth.v1.ModelType`
        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.ModelFile`
        :param shareable: 是否打开组织共享
        :type shareable: bool
        :param base_model_id: 基模型id
        :type base_model_id: str
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._file = None
        self._shareable = None
        self._base_model_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        self.file = file
        if shareable is not None:
            self.shareable = shareable
        if base_model_id is not None:
            self.base_model_id = base_model_id

    @property
    def name(self):
        r"""Gets the name of this CreateModelReq.

        模型名称，取值范围：[5,32]，允许大小写字母、数字、下划线(_)、中划线(-)和空格,只能以字母开头

        :return: The name of this CreateModelReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateModelReq.

        模型名称，取值范围：[5,32]，允许大小写字母、数字、下划线(_)、中划线(-)和空格,只能以字母开头

        :param name: The name of this CreateModelReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateModelReq.

        模型描述信息

        :return: The description of this CreateModelReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateModelReq.

        模型描述信息

        :param description: The description of this CreateModelReq.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this CreateModelReq.

        :return: The type of this CreateModelReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ModelType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateModelReq.

        :param type: The type of this CreateModelReq.
        :type type: :class:`huaweicloudsdkeihealth.v1.ModelType`
        """
        self._type = type

    @property
    def file(self):
        r"""Gets the file of this CreateModelReq.

        :return: The file of this CreateModelReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ModelFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this CreateModelReq.

        :param file: The file of this CreateModelReq.
        :type file: :class:`huaweicloudsdkeihealth.v1.ModelFile`
        """
        self._file = file

    @property
    def shareable(self):
        r"""Gets the shareable of this CreateModelReq.

        是否打开组织共享

        :return: The shareable of this CreateModelReq.
        :rtype: bool
        """
        return self._shareable

    @shareable.setter
    def shareable(self, shareable):
        r"""Sets the shareable of this CreateModelReq.

        是否打开组织共享

        :param shareable: The shareable of this CreateModelReq.
        :type shareable: bool
        """
        self._shareable = shareable

    @property
    def base_model_id(self):
        r"""Gets the base_model_id of this CreateModelReq.

        基模型id

        :return: The base_model_id of this CreateModelReq.
        :rtype: str
        """
        return self._base_model_id

    @base_model_id.setter
    def base_model_id(self, base_model_id):
        r"""Sets the base_model_id of this CreateModelReq.

        基模型id

        :param base_model_id: The base_model_id of this CreateModelReq.
        :type base_model_id: str
        """
        self._base_model_id = base_model_id

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
        if not isinstance(other, CreateModelReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
