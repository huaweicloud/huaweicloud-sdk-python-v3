# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataServiceInstanceAccesslogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'instance_id': 'str',
        'is_api': 'bool'
    }

    attribute_map = {
        'workspace': 'workspace',
        'instance_id': 'instance_id',
        'is_api': 'is_api'
    }

    def __init__(self, workspace=None, instance_id=None, is_api=None):
        r"""ListDataServiceInstanceAccesslogsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param instance_id: 集群ID编号。
        :type instance_id: str
        :param is_api: 是否查询API的访问日志，true表示查询API的访问日志，false表示查询应用的访问日志。
        :type is_api: bool
        """
        
        

        self._workspace = None
        self._instance_id = None
        self._is_api = None
        self.discriminator = None

        self.workspace = workspace
        self.instance_id = instance_id
        if is_api is not None:
            self.is_api = is_api

    @property
    def workspace(self):
        r"""Gets the workspace of this ListDataServiceInstanceAccesslogsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListDataServiceInstanceAccesslogsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListDataServiceInstanceAccesslogsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListDataServiceInstanceAccesslogsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListDataServiceInstanceAccesslogsRequest.

        集群ID编号。

        :return: The instance_id of this ListDataServiceInstanceAccesslogsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListDataServiceInstanceAccesslogsRequest.

        集群ID编号。

        :param instance_id: The instance_id of this ListDataServiceInstanceAccesslogsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def is_api(self):
        r"""Gets the is_api of this ListDataServiceInstanceAccesslogsRequest.

        是否查询API的访问日志，true表示查询API的访问日志，false表示查询应用的访问日志。

        :return: The is_api of this ListDataServiceInstanceAccesslogsRequest.
        :rtype: bool
        """
        return self._is_api

    @is_api.setter
    def is_api(self, is_api):
        r"""Sets the is_api of this ListDataServiceInstanceAccesslogsRequest.

        是否查询API的访问日志，true表示查询API的访问日志，false表示查询应用的访问日志。

        :param is_api: The is_api of this ListDataServiceInstanceAccesslogsRequest.
        :type is_api: bool
        """
        self._is_api = is_api

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
        if not isinstance(other, ListDataServiceInstanceAccesslogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
