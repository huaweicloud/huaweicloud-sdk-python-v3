# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSlowLogExportTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'cur_page': 'int',
        'per_page': 'int',
        'export_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'cur_page': 'cur_page',
        'per_page': 'per_page',
        'export_type': 'export_type'
    }

    def __init__(self, instance_id=None, cur_page=None, per_page=None, export_type=None):
        r"""ListSlowLogExportTaskRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param cur_page: 页码
        :type cur_page: int
        :param per_page: 每页记录数
        :type per_page: int
        :param export_type: 导出类型，取值范围：slowsql、slowsqldetails
        :type export_type: str
        """
        
        

        self._instance_id = None
        self._cur_page = None
        self._per_page = None
        self._export_type = None
        self.discriminator = None

        self.instance_id = instance_id
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page
        if export_type is not None:
            self.export_type = export_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSlowLogExportTaskRequest.

        实例ID

        :return: The instance_id of this ListSlowLogExportTaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSlowLogExportTaskRequest.

        实例ID

        :param instance_id: The instance_id of this ListSlowLogExportTaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListSlowLogExportTaskRequest.

        页码

        :return: The cur_page of this ListSlowLogExportTaskRequest.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListSlowLogExportTaskRequest.

        页码

        :param cur_page: The cur_page of this ListSlowLogExportTaskRequest.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ListSlowLogExportTaskRequest.

        每页记录数

        :return: The per_page of this ListSlowLogExportTaskRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListSlowLogExportTaskRequest.

        每页记录数

        :param per_page: The per_page of this ListSlowLogExportTaskRequest.
        :type per_page: int
        """
        self._per_page = per_page

    @property
    def export_type(self):
        r"""Gets the export_type of this ListSlowLogExportTaskRequest.

        导出类型，取值范围：slowsql、slowsqldetails

        :return: The export_type of this ListSlowLogExportTaskRequest.
        :rtype: str
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        r"""Sets the export_type of this ListSlowLogExportTaskRequest.

        导出类型，取值范围：slowsql、slowsqldetails

        :param export_type: The export_type of this ListSlowLogExportTaskRequest.
        :type export_type: str
        """
        self._export_type = export_type

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
        if not isinstance(other, ListSlowLogExportTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
