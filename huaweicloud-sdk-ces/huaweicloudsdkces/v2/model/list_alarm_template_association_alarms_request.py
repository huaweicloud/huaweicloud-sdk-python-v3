# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmTemplateAssociationAlarmsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'template_id': 'template_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, template_id=None, offset=None, limit=None):
        r"""ListAlarmTemplateAssociationAlarmsRequest

        The model defined in huaweicloud sdk

        :param template_id: 告警模板的ID，以at开头，后跟字母、数字，长度最长为64
        :type template_id: str
        :param offset: 分页查询时查询的起始位置，表示从第几条数据开始，默认为0
        :type offset: int
        :param limit: 查询结果条数的限制值，取值范围为[1,100]，默认值为100
        :type limit: int
        """
        
        

        self._template_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.template_id = template_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def template_id(self):
        r"""Gets the template_id of this ListAlarmTemplateAssociationAlarmsRequest.

        告警模板的ID，以at开头，后跟字母、数字，长度最长为64

        :return: The template_id of this ListAlarmTemplateAssociationAlarmsRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ListAlarmTemplateAssociationAlarmsRequest.

        告警模板的ID，以at开头，后跟字母、数字，长度最长为64

        :param template_id: The template_id of this ListAlarmTemplateAssociationAlarmsRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAlarmTemplateAssociationAlarmsRequest.

        分页查询时查询的起始位置，表示从第几条数据开始，默认为0

        :return: The offset of this ListAlarmTemplateAssociationAlarmsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlarmTemplateAssociationAlarmsRequest.

        分页查询时查询的起始位置，表示从第几条数据开始，默认为0

        :param offset: The offset of this ListAlarmTemplateAssociationAlarmsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAlarmTemplateAssociationAlarmsRequest.

        查询结果条数的限制值，取值范围为[1,100]，默认值为100

        :return: The limit of this ListAlarmTemplateAssociationAlarmsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlarmTemplateAssociationAlarmsRequest.

        查询结果条数的限制值，取值范围为[1,100]，默认值为100

        :param limit: The limit of this ListAlarmTemplateAssociationAlarmsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAlarmTemplateAssociationAlarmsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
