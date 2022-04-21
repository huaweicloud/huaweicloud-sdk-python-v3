# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportApiDefinitionsV2RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_create_group': 'bool',
        'group_id': 'str',
        'app_id': 'str',
        'extend_mode': 'str',
        'simple_mode': 'bool',
        'mock_mode': 'bool',
        'api_mode': 'str',
        'file_name': 'file'
    }

    attribute_map = {
        'is_create_group': 'is_create_group',
        'group_id': 'group_id',
        'app_id': 'app_id',
        'extend_mode': 'extend_mode',
        'simple_mode': 'simple_mode',
        'mock_mode': 'mock_mode',
        'api_mode': 'api_mode',
        'file_name': 'file_name'
    }

    def __init__(self, is_create_group=None, group_id=None, app_id=None, extend_mode=None, simple_mode=None, mock_mode=None, api_mode=None, file_name=None):
        """ImportApiDefinitionsV2RequestBody

        The model defined in huaweicloud sdk

        :param is_create_group: 是否创建新分组
        :type is_create_group: bool
        :param group_id: API分组编号。  当is_create_group&#x3D;false时为必填
        :type group_id: str
        :param app_id: 应用编号。  当is_create_group&#x3D;false且使用集成应用分组时必填
        :type app_id: str
        :param extend_mode: 扩展信息导入模式 - merge：当扩展信息定义冲突时，merge保留原有扩展信息 - override：当扩展信息定义冲突时，override会覆盖原有扩展信息
        :type extend_mode: str
        :param simple_mode: 是否开启简易导入模式
        :type simple_mode: bool
        :param mock_mode: 是否开启Mock后端
        :type mock_mode: bool
        :param api_mode: 导入模式 - merge：当API信息定义冲突时，merge保留原有API信息 - override：当API信息定义冲突时，override会覆盖原有API信息
        :type api_mode: str
        :param file_name: 导入Api的请求体，json或yaml格式的文件
        :type file_name: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._is_create_group = None
        self._group_id = None
        self._app_id = None
        self._extend_mode = None
        self._simple_mode = None
        self._mock_mode = None
        self._api_mode = None
        self._file_name = None
        self.discriminator = None

        if is_create_group is not None:
            self.is_create_group = is_create_group
        if group_id is not None:
            self.group_id = group_id
        if app_id is not None:
            self.app_id = app_id
        if extend_mode is not None:
            self.extend_mode = extend_mode
        if simple_mode is not None:
            self.simple_mode = simple_mode
        if mock_mode is not None:
            self.mock_mode = mock_mode
        if api_mode is not None:
            self.api_mode = api_mode
        self.file_name = file_name

    @property
    def is_create_group(self):
        """Gets the is_create_group of this ImportApiDefinitionsV2RequestBody.

        是否创建新分组

        :return: The is_create_group of this ImportApiDefinitionsV2RequestBody.
        :rtype: bool
        """
        return self._is_create_group

    @is_create_group.setter
    def is_create_group(self, is_create_group):
        """Sets the is_create_group of this ImportApiDefinitionsV2RequestBody.

        是否创建新分组

        :param is_create_group: The is_create_group of this ImportApiDefinitionsV2RequestBody.
        :type is_create_group: bool
        """
        self._is_create_group = is_create_group

    @property
    def group_id(self):
        """Gets the group_id of this ImportApiDefinitionsV2RequestBody.

        API分组编号。  当is_create_group=false时为必填

        :return: The group_id of this ImportApiDefinitionsV2RequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ImportApiDefinitionsV2RequestBody.

        API分组编号。  当is_create_group=false时为必填

        :param group_id: The group_id of this ImportApiDefinitionsV2RequestBody.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def app_id(self):
        """Gets the app_id of this ImportApiDefinitionsV2RequestBody.

        应用编号。  当is_create_group=false且使用集成应用分组时必填

        :return: The app_id of this ImportApiDefinitionsV2RequestBody.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ImportApiDefinitionsV2RequestBody.

        应用编号。  当is_create_group=false且使用集成应用分组时必填

        :param app_id: The app_id of this ImportApiDefinitionsV2RequestBody.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def extend_mode(self):
        """Gets the extend_mode of this ImportApiDefinitionsV2RequestBody.

        扩展信息导入模式 - merge：当扩展信息定义冲突时，merge保留原有扩展信息 - override：当扩展信息定义冲突时，override会覆盖原有扩展信息

        :return: The extend_mode of this ImportApiDefinitionsV2RequestBody.
        :rtype: str
        """
        return self._extend_mode

    @extend_mode.setter
    def extend_mode(self, extend_mode):
        """Sets the extend_mode of this ImportApiDefinitionsV2RequestBody.

        扩展信息导入模式 - merge：当扩展信息定义冲突时，merge保留原有扩展信息 - override：当扩展信息定义冲突时，override会覆盖原有扩展信息

        :param extend_mode: The extend_mode of this ImportApiDefinitionsV2RequestBody.
        :type extend_mode: str
        """
        self._extend_mode = extend_mode

    @property
    def simple_mode(self):
        """Gets the simple_mode of this ImportApiDefinitionsV2RequestBody.

        是否开启简易导入模式

        :return: The simple_mode of this ImportApiDefinitionsV2RequestBody.
        :rtype: bool
        """
        return self._simple_mode

    @simple_mode.setter
    def simple_mode(self, simple_mode):
        """Sets the simple_mode of this ImportApiDefinitionsV2RequestBody.

        是否开启简易导入模式

        :param simple_mode: The simple_mode of this ImportApiDefinitionsV2RequestBody.
        :type simple_mode: bool
        """
        self._simple_mode = simple_mode

    @property
    def mock_mode(self):
        """Gets the mock_mode of this ImportApiDefinitionsV2RequestBody.

        是否开启Mock后端

        :return: The mock_mode of this ImportApiDefinitionsV2RequestBody.
        :rtype: bool
        """
        return self._mock_mode

    @mock_mode.setter
    def mock_mode(self, mock_mode):
        """Sets the mock_mode of this ImportApiDefinitionsV2RequestBody.

        是否开启Mock后端

        :param mock_mode: The mock_mode of this ImportApiDefinitionsV2RequestBody.
        :type mock_mode: bool
        """
        self._mock_mode = mock_mode

    @property
    def api_mode(self):
        """Gets the api_mode of this ImportApiDefinitionsV2RequestBody.

        导入模式 - merge：当API信息定义冲突时，merge保留原有API信息 - override：当API信息定义冲突时，override会覆盖原有API信息

        :return: The api_mode of this ImportApiDefinitionsV2RequestBody.
        :rtype: str
        """
        return self._api_mode

    @api_mode.setter
    def api_mode(self, api_mode):
        """Sets the api_mode of this ImportApiDefinitionsV2RequestBody.

        导入模式 - merge：当API信息定义冲突时，merge保留原有API信息 - override：当API信息定义冲突时，override会覆盖原有API信息

        :param api_mode: The api_mode of this ImportApiDefinitionsV2RequestBody.
        :type api_mode: str
        """
        self._api_mode = api_mode

    @property
    def file_name(self):
        """Gets the file_name of this ImportApiDefinitionsV2RequestBody.

        导入Api的请求体，json或yaml格式的文件

        :return: The file_name of this ImportApiDefinitionsV2RequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ImportApiDefinitionsV2RequestBody.

        导入Api的请求体，json或yaml格式的文件

        :param file_name: The file_name of this ImportApiDefinitionsV2RequestBody.
        :type file_name: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file_name = file_name

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
        if not isinstance(other, ImportApiDefinitionsV2RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
