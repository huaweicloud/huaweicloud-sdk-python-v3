# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSignatureFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_id': 'str',
        'file_name': 'str',
        'file_ref': 'int',
        'file_size': 'int',
        'file_type': 'int',
        'module_type': 'int',
        'operator': 'str',
        'file_desc': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'file_id': 'file_id',
        'file_name': 'file_name',
        'file_ref': 'file_ref',
        'file_size': 'file_size',
        'file_type': 'file_type',
        'module_type': 'module_type',
        'operator': 'operator',
        'file_desc': 'file_desc',
        'update_time': 'update_time'
    }

    def __init__(self, file_id=None, file_name=None, file_ref=None, file_size=None, file_type=None, module_type=None, operator=None, file_desc=None, update_time=None):
        r"""ShowSignatureFileResponse

        The model defined in huaweicloud sdk

        :param file_id: 文件ID
        :type file_id: str
        :param file_name: 文件名称
        :type file_name: str
        :param file_ref: 文件引用
        :type file_ref: int
        :param file_size: 文件大小
        :type file_size: int
        :param file_type: 文件类型
        :type file_type: int
        :param module_type: 模块类型
        :type module_type: int
        :param operator: 操作人
        :type operator: str
        :param file_desc: 描述
        :type file_desc: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        super(ShowSignatureFileResponse, self).__init__()

        self._file_id = None
        self._file_name = None
        self._file_ref = None
        self._file_size = None
        self._file_type = None
        self._module_type = None
        self._operator = None
        self._file_desc = None
        self._update_time = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if file_name is not None:
            self.file_name = file_name
        if file_ref is not None:
            self.file_ref = file_ref
        if file_size is not None:
            self.file_size = file_size
        if file_type is not None:
            self.file_type = file_type
        if module_type is not None:
            self.module_type = module_type
        if operator is not None:
            self.operator = operator
        if file_desc is not None:
            self.file_desc = file_desc
        if update_time is not None:
            self.update_time = update_time

    @property
    def file_id(self):
        r"""Gets the file_id of this ShowSignatureFileResponse.

        文件ID

        :return: The file_id of this ShowSignatureFileResponse.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this ShowSignatureFileResponse.

        文件ID

        :param file_id: The file_id of this ShowSignatureFileResponse.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def file_name(self):
        r"""Gets the file_name of this ShowSignatureFileResponse.

        文件名称

        :return: The file_name of this ShowSignatureFileResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ShowSignatureFileResponse.

        文件名称

        :param file_name: The file_name of this ShowSignatureFileResponse.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_ref(self):
        r"""Gets the file_ref of this ShowSignatureFileResponse.

        文件引用

        :return: The file_ref of this ShowSignatureFileResponse.
        :rtype: int
        """
        return self._file_ref

    @file_ref.setter
    def file_ref(self, file_ref):
        r"""Sets the file_ref of this ShowSignatureFileResponse.

        文件引用

        :param file_ref: The file_ref of this ShowSignatureFileResponse.
        :type file_ref: int
        """
        self._file_ref = file_ref

    @property
    def file_size(self):
        r"""Gets the file_size of this ShowSignatureFileResponse.

        文件大小

        :return: The file_size of this ShowSignatureFileResponse.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this ShowSignatureFileResponse.

        文件大小

        :param file_size: The file_size of this ShowSignatureFileResponse.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_type(self):
        r"""Gets the file_type of this ShowSignatureFileResponse.

        文件类型

        :return: The file_type of this ShowSignatureFileResponse.
        :rtype: int
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ShowSignatureFileResponse.

        文件类型

        :param file_type: The file_type of this ShowSignatureFileResponse.
        :type file_type: int
        """
        self._file_type = file_type

    @property
    def module_type(self):
        r"""Gets the module_type of this ShowSignatureFileResponse.

        模块类型

        :return: The module_type of this ShowSignatureFileResponse.
        :rtype: int
        """
        return self._module_type

    @module_type.setter
    def module_type(self, module_type):
        r"""Sets the module_type of this ShowSignatureFileResponse.

        模块类型

        :param module_type: The module_type of this ShowSignatureFileResponse.
        :type module_type: int
        """
        self._module_type = module_type

    @property
    def operator(self):
        r"""Gets the operator of this ShowSignatureFileResponse.

        操作人

        :return: The operator of this ShowSignatureFileResponse.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ShowSignatureFileResponse.

        操作人

        :param operator: The operator of this ShowSignatureFileResponse.
        :type operator: str
        """
        self._operator = operator

    @property
    def file_desc(self):
        r"""Gets the file_desc of this ShowSignatureFileResponse.

        描述

        :return: The file_desc of this ShowSignatureFileResponse.
        :rtype: str
        """
        return self._file_desc

    @file_desc.setter
    def file_desc(self, file_desc):
        r"""Sets the file_desc of this ShowSignatureFileResponse.

        描述

        :param file_desc: The file_desc of this ShowSignatureFileResponse.
        :type file_desc: str
        """
        self._file_desc = file_desc

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowSignatureFileResponse.

        更新时间

        :return: The update_time of this ShowSignatureFileResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowSignatureFileResponse.

        更新时间

        :param update_time: The update_time of this ShowSignatureFileResponse.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, ShowSignatureFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
