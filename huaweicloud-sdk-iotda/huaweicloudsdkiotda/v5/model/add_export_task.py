# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddExportTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_condition': 'object',
        'export_format': 'str',
        'app_type': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_condition': 'resource_condition',
        'export_format': 'export_format',
        'app_type': 'app_type',
        'app_id': 'app_id'
    }

    def __init__(self, resource_type=None, resource_condition=None, export_format=None, app_type=None, app_id=None):
        r"""AddExportTask

        The model defined in huaweicloud sdk

        :param resource_type: 导出源资源类型，支持批量任务导出类型BatchTask。
        :type resource_type: str
        :param resource_condition: 资源过滤条件，Json 格式，里面是(K,V)键值对，当resource_type为BatchTask时填写填写key为task_id，value为BatchTask的task_id(task_id从批量任务接口获得)。
        :type resource_condition: object
        :param export_format: 导出格式，目前仅支持xls格式,默认格式为xls.(注意下载的文件已使用zip打包，后缀为&#39;.zip&#39;，此处格式指的导出内容承载格式)
        :type export_format: str
        :param app_type: 租户规则的生效范围，默认GLOBAL，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为应用级，如果类型为APP，需要携带app_id，如果不带，生效范围为defaultApp。 
        :type app_type: str
        :param app_id: 应用ID。此参数为非必选参数，用于兼容平台老用户存在多应用的场景。存在多应用的用户需要使用该接口时，必须携带该参数指定创建的规则归属到哪个应用下，否则接口会提示错误。如果用户存在多应用，同时又不想携带该参数，可以联系华为技术支持对用户数据做应用合并。
        :type app_id: str
        """
        
        

        self._resource_type = None
        self._resource_condition = None
        self._export_format = None
        self._app_type = None
        self._app_id = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_condition = resource_condition
        if export_format is not None:
            self.export_format = export_format
        if app_type is not None:
            self.app_type = app_type
        if app_id is not None:
            self.app_id = app_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this AddExportTask.

        导出源资源类型，支持批量任务导出类型BatchTask。

        :return: The resource_type of this AddExportTask.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this AddExportTask.

        导出源资源类型，支持批量任务导出类型BatchTask。

        :param resource_type: The resource_type of this AddExportTask.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_condition(self):
        r"""Gets the resource_condition of this AddExportTask.

        资源过滤条件，Json 格式，里面是(K,V)键值对，当resource_type为BatchTask时填写填写key为task_id，value为BatchTask的task_id(task_id从批量任务接口获得)。

        :return: The resource_condition of this AddExportTask.
        :rtype: object
        """
        return self._resource_condition

    @resource_condition.setter
    def resource_condition(self, resource_condition):
        r"""Sets the resource_condition of this AddExportTask.

        资源过滤条件，Json 格式，里面是(K,V)键值对，当resource_type为BatchTask时填写填写key为task_id，value为BatchTask的task_id(task_id从批量任务接口获得)。

        :param resource_condition: The resource_condition of this AddExportTask.
        :type resource_condition: object
        """
        self._resource_condition = resource_condition

    @property
    def export_format(self):
        r"""Gets the export_format of this AddExportTask.

        导出格式，目前仅支持xls格式,默认格式为xls.(注意下载的文件已使用zip打包，后缀为'.zip'，此处格式指的导出内容承载格式)

        :return: The export_format of this AddExportTask.
        :rtype: str
        """
        return self._export_format

    @export_format.setter
    def export_format(self, export_format):
        r"""Sets the export_format of this AddExportTask.

        导出格式，目前仅支持xls格式,默认格式为xls.(注意下载的文件已使用zip打包，后缀为'.zip'，此处格式指的导出内容承载格式)

        :param export_format: The export_format of this AddExportTask.
        :type export_format: str
        """
        self._export_format = export_format

    @property
    def app_type(self):
        r"""Gets the app_type of this AddExportTask.

        租户规则的生效范围，默认GLOBAL，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为应用级，如果类型为APP，需要携带app_id，如果不带，生效范围为defaultApp。 

        :return: The app_type of this AddExportTask.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this AddExportTask.

        租户规则的生效范围，默认GLOBAL，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为应用级，如果类型为APP，需要携带app_id，如果不带，生效范围为defaultApp。 

        :param app_type: The app_type of this AddExportTask.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def app_id(self):
        r"""Gets the app_id of this AddExportTask.

        应用ID。此参数为非必选参数，用于兼容平台老用户存在多应用的场景。存在多应用的用户需要使用该接口时，必须携带该参数指定创建的规则归属到哪个应用下，否则接口会提示错误。如果用户存在多应用，同时又不想携带该参数，可以联系华为技术支持对用户数据做应用合并。

        :return: The app_id of this AddExportTask.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this AddExportTask.

        应用ID。此参数为非必选参数，用于兼容平台老用户存在多应用的场景。存在多应用的用户需要使用该接口时，必须携带该参数指定创建的规则归属到哪个应用下，否则接口会提示错误。如果用户存在多应用，同时又不想携带该参数，可以联系华为技术支持对用户数据做应用合并。

        :param app_id: The app_id of this AddExportTask.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, AddExportTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
