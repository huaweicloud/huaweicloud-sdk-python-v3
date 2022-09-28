# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportTemplateResultRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'source_project_id': 'str',
        'source_template_id': 'str',
        'destination_template_id': 'str',
        'destination_template_name': 'str',
        'failed_reason': 'str',
        'status': 'str'
    }

    attribute_map = {
        'source_project_id': 'source_project_id',
        'source_template_id': 'source_template_id',
        'destination_template_id': 'destination_template_id',
        'destination_template_name': 'destination_template_name',
        'failed_reason': 'failed_reason',
        'status': 'status'
    }

    def __init__(self, source_project_id=None, source_template_id=None, destination_template_id=None, destination_template_name=None, failed_reason=None, status=None):
        """ImportTemplateResultRsp

        The model defined in huaweicloud sdk

        :param source_project_id: 源项目id
        :type source_project_id: str
        :param source_template_id: 源模板id
        :type source_template_id: str
        :param destination_template_id: 导入后的模板id
        :type destination_template_id: str
        :param destination_template_name: 导入后的模板名称
        :type destination_template_name: str
        :param failed_reason: 失败原因，导入失败会返回
        :type failed_reason: str
        :param status: 导入结果
        :type status: str
        """
        
        

        self._source_project_id = None
        self._source_template_id = None
        self._destination_template_id = None
        self._destination_template_name = None
        self._failed_reason = None
        self._status = None
        self.discriminator = None

        if source_project_id is not None:
            self.source_project_id = source_project_id
        if source_template_id is not None:
            self.source_template_id = source_template_id
        if destination_template_id is not None:
            self.destination_template_id = destination_template_id
        if destination_template_name is not None:
            self.destination_template_name = destination_template_name
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if status is not None:
            self.status = status

    @property
    def source_project_id(self):
        """Gets the source_project_id of this ImportTemplateResultRsp.

        源项目id

        :return: The source_project_id of this ImportTemplateResultRsp.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        """Sets the source_project_id of this ImportTemplateResultRsp.

        源项目id

        :param source_project_id: The source_project_id of this ImportTemplateResultRsp.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def source_template_id(self):
        """Gets the source_template_id of this ImportTemplateResultRsp.

        源模板id

        :return: The source_template_id of this ImportTemplateResultRsp.
        :rtype: str
        """
        return self._source_template_id

    @source_template_id.setter
    def source_template_id(self, source_template_id):
        """Sets the source_template_id of this ImportTemplateResultRsp.

        源模板id

        :param source_template_id: The source_template_id of this ImportTemplateResultRsp.
        :type source_template_id: str
        """
        self._source_template_id = source_template_id

    @property
    def destination_template_id(self):
        """Gets the destination_template_id of this ImportTemplateResultRsp.

        导入后的模板id

        :return: The destination_template_id of this ImportTemplateResultRsp.
        :rtype: str
        """
        return self._destination_template_id

    @destination_template_id.setter
    def destination_template_id(self, destination_template_id):
        """Sets the destination_template_id of this ImportTemplateResultRsp.

        导入后的模板id

        :param destination_template_id: The destination_template_id of this ImportTemplateResultRsp.
        :type destination_template_id: str
        """
        self._destination_template_id = destination_template_id

    @property
    def destination_template_name(self):
        """Gets the destination_template_name of this ImportTemplateResultRsp.

        导入后的模板名称

        :return: The destination_template_name of this ImportTemplateResultRsp.
        :rtype: str
        """
        return self._destination_template_name

    @destination_template_name.setter
    def destination_template_name(self, destination_template_name):
        """Sets the destination_template_name of this ImportTemplateResultRsp.

        导入后的模板名称

        :param destination_template_name: The destination_template_name of this ImportTemplateResultRsp.
        :type destination_template_name: str
        """
        self._destination_template_name = destination_template_name

    @property
    def failed_reason(self):
        """Gets the failed_reason of this ImportTemplateResultRsp.

        失败原因，导入失败会返回

        :return: The failed_reason of this ImportTemplateResultRsp.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this ImportTemplateResultRsp.

        失败原因，导入失败会返回

        :param failed_reason: The failed_reason of this ImportTemplateResultRsp.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def status(self):
        """Gets the status of this ImportTemplateResultRsp.

        导入结果

        :return: The status of this ImportTemplateResultRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ImportTemplateResultRsp.

        导入结果

        :param status: The status of this ImportTemplateResultRsp.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ImportTemplateResultRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
