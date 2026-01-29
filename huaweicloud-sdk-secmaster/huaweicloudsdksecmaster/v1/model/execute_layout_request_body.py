# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteLayoutRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'ids': 'str',
        'upload_file': 'file'
    }

    attribute_map = {
        'action': 'action',
        'ids': 'ids',
        'upload_file': 'uploadFile'
    }

    def __init__(self, action=None, ids=None, upload_file=None):
        r"""ExecuteLayoutRequestBody

        The model defined in huaweicloud sdk

        :param action: 对布局的操作 VERIFY 校验导入布局压缩包文件 IMPORT  导入布局压缩包文件 EXPORT 导出布局文件
        :type action: str
        :param ids: 操作布局的id列表
        :type ids: str
        :param upload_file: 上传的文件
        :type upload_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._action = None
        self._ids = None
        self._upload_file = None
        self.discriminator = None

        self.action = action
        if ids is not None:
            self.ids = ids
        if upload_file is not None:
            self.upload_file = upload_file

    @property
    def action(self):
        r"""Gets the action of this ExecuteLayoutRequestBody.

        对布局的操作 VERIFY 校验导入布局压缩包文件 IMPORT  导入布局压缩包文件 EXPORT 导出布局文件

        :return: The action of this ExecuteLayoutRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ExecuteLayoutRequestBody.

        对布局的操作 VERIFY 校验导入布局压缩包文件 IMPORT  导入布局压缩包文件 EXPORT 导出布局文件

        :param action: The action of this ExecuteLayoutRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def ids(self):
        r"""Gets the ids of this ExecuteLayoutRequestBody.

        操作布局的id列表

        :return: The ids of this ExecuteLayoutRequestBody.
        :rtype: str
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this ExecuteLayoutRequestBody.

        操作布局的id列表

        :param ids: The ids of this ExecuteLayoutRequestBody.
        :type ids: str
        """
        self._ids = ids

    @property
    def upload_file(self):
        r"""Gets the upload_file of this ExecuteLayoutRequestBody.

        上传的文件

        :return: The upload_file of this ExecuteLayoutRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._upload_file

    @upload_file.setter
    def upload_file(self, upload_file):
        r"""Sets the upload_file of this ExecuteLayoutRequestBody.

        上传的文件

        :param upload_file: The upload_file of this ExecuteLayoutRequestBody.
        :type upload_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._upload_file = upload_file

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
        if not isinstance(other, ExecuteLayoutRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
