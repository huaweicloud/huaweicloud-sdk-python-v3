# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareResultInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'objects_compare_overview_info': 'ObjectsCompareTaskInfo',
        'objects_compare_detail_infos': 'list[ObjectsCompareDetailInfo]',
        'data_compare_task_list': 'list[CompareJobInfo]',
        'line_compare_overview_infos': 'list[LineCompareOverviewInfo]',
        'line_compare_detail_infos': 'list[TableLineCompareDetailInfo]',
        'content_compare_overview_infos': 'list[ContentCompareOverviewInfo]',
        'content_compare_detail_infos': 'list[ContentCompareDetailInfo]'
    }

    attribute_map = {
        'objects_compare_overview_info': 'objects_compare_overview_info',
        'objects_compare_detail_infos': 'objects_compare_detail_infos',
        'data_compare_task_list': 'data_compare_task_list',
        'line_compare_overview_infos': 'line_compare_overview_infos',
        'line_compare_detail_infos': 'line_compare_detail_infos',
        'content_compare_overview_infos': 'content_compare_overview_infos',
        'content_compare_detail_infos': 'content_compare_detail_infos'
    }

    def __init__(self, objects_compare_overview_info=None, objects_compare_detail_infos=None, data_compare_task_list=None, line_compare_overview_infos=None, line_compare_detail_infos=None, content_compare_overview_infos=None, content_compare_detail_infos=None):
        """CompareResultInfo

        The model defined in huaweicloud sdk

        :param objects_compare_overview_info: 
        :type objects_compare_overview_info: :class:`huaweicloudsdkdrs.v5.ObjectsCompareTaskInfo`
        :param objects_compare_detail_infos: 对象级对比详情信息体。
        :type objects_compare_detail_infos: list[:class:`huaweicloudsdkdrs.v5.ObjectsCompareDetailInfo`]
        :param data_compare_task_list: 数据对比任务列表。
        :type data_compare_task_list: list[:class:`huaweicloudsdkdrs.v5.CompareJobInfo`]
        :param line_compare_overview_infos: 行数对比概览信息体。
        :type line_compare_overview_infos: list[:class:`huaweicloudsdkdrs.v5.LineCompareOverviewInfo`]
        :param line_compare_detail_infos: 行数对比任务表级详情。
        :type line_compare_detail_infos: list[:class:`huaweicloudsdkdrs.v5.TableLineCompareDetailInfo`]
        :param content_compare_overview_infos: 内容对比概览信息体。
        :type content_compare_overview_infos: list[:class:`huaweicloudsdkdrs.v5.ContentCompareOverviewInfo`]
        :param content_compare_detail_infos: 内容对比详情信息体。
        :type content_compare_detail_infos: list[:class:`huaweicloudsdkdrs.v5.ContentCompareDetailInfo`]
        """
        
        

        self._objects_compare_overview_info = None
        self._objects_compare_detail_infos = None
        self._data_compare_task_list = None
        self._line_compare_overview_infos = None
        self._line_compare_detail_infos = None
        self._content_compare_overview_infos = None
        self._content_compare_detail_infos = None
        self.discriminator = None

        if objects_compare_overview_info is not None:
            self.objects_compare_overview_info = objects_compare_overview_info
        if objects_compare_detail_infos is not None:
            self.objects_compare_detail_infos = objects_compare_detail_infos
        if data_compare_task_list is not None:
            self.data_compare_task_list = data_compare_task_list
        if line_compare_overview_infos is not None:
            self.line_compare_overview_infos = line_compare_overview_infos
        if line_compare_detail_infos is not None:
            self.line_compare_detail_infos = line_compare_detail_infos
        if content_compare_overview_infos is not None:
            self.content_compare_overview_infos = content_compare_overview_infos
        if content_compare_detail_infos is not None:
            self.content_compare_detail_infos = content_compare_detail_infos

    @property
    def objects_compare_overview_info(self):
        """Gets the objects_compare_overview_info of this CompareResultInfo.

        :return: The objects_compare_overview_info of this CompareResultInfo.
        :rtype: :class:`huaweicloudsdkdrs.v5.ObjectsCompareTaskInfo`
        """
        return self._objects_compare_overview_info

    @objects_compare_overview_info.setter
    def objects_compare_overview_info(self, objects_compare_overview_info):
        """Sets the objects_compare_overview_info of this CompareResultInfo.

        :param objects_compare_overview_info: The objects_compare_overview_info of this CompareResultInfo.
        :type objects_compare_overview_info: :class:`huaweicloudsdkdrs.v5.ObjectsCompareTaskInfo`
        """
        self._objects_compare_overview_info = objects_compare_overview_info

    @property
    def objects_compare_detail_infos(self):
        """Gets the objects_compare_detail_infos of this CompareResultInfo.

        对象级对比详情信息体。

        :return: The objects_compare_detail_infos of this CompareResultInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ObjectsCompareDetailInfo`]
        """
        return self._objects_compare_detail_infos

    @objects_compare_detail_infos.setter
    def objects_compare_detail_infos(self, objects_compare_detail_infos):
        """Sets the objects_compare_detail_infos of this CompareResultInfo.

        对象级对比详情信息体。

        :param objects_compare_detail_infos: The objects_compare_detail_infos of this CompareResultInfo.
        :type objects_compare_detail_infos: list[:class:`huaweicloudsdkdrs.v5.ObjectsCompareDetailInfo`]
        """
        self._objects_compare_detail_infos = objects_compare_detail_infos

    @property
    def data_compare_task_list(self):
        """Gets the data_compare_task_list of this CompareResultInfo.

        数据对比任务列表。

        :return: The data_compare_task_list of this CompareResultInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.CompareJobInfo`]
        """
        return self._data_compare_task_list

    @data_compare_task_list.setter
    def data_compare_task_list(self, data_compare_task_list):
        """Sets the data_compare_task_list of this CompareResultInfo.

        数据对比任务列表。

        :param data_compare_task_list: The data_compare_task_list of this CompareResultInfo.
        :type data_compare_task_list: list[:class:`huaweicloudsdkdrs.v5.CompareJobInfo`]
        """
        self._data_compare_task_list = data_compare_task_list

    @property
    def line_compare_overview_infos(self):
        """Gets the line_compare_overview_infos of this CompareResultInfo.

        行数对比概览信息体。

        :return: The line_compare_overview_infos of this CompareResultInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.LineCompareOverviewInfo`]
        """
        return self._line_compare_overview_infos

    @line_compare_overview_infos.setter
    def line_compare_overview_infos(self, line_compare_overview_infos):
        """Sets the line_compare_overview_infos of this CompareResultInfo.

        行数对比概览信息体。

        :param line_compare_overview_infos: The line_compare_overview_infos of this CompareResultInfo.
        :type line_compare_overview_infos: list[:class:`huaweicloudsdkdrs.v5.LineCompareOverviewInfo`]
        """
        self._line_compare_overview_infos = line_compare_overview_infos

    @property
    def line_compare_detail_infos(self):
        """Gets the line_compare_detail_infos of this CompareResultInfo.

        行数对比任务表级详情。

        :return: The line_compare_detail_infos of this CompareResultInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.TableLineCompareDetailInfo`]
        """
        return self._line_compare_detail_infos

    @line_compare_detail_infos.setter
    def line_compare_detail_infos(self, line_compare_detail_infos):
        """Sets the line_compare_detail_infos of this CompareResultInfo.

        行数对比任务表级详情。

        :param line_compare_detail_infos: The line_compare_detail_infos of this CompareResultInfo.
        :type line_compare_detail_infos: list[:class:`huaweicloudsdkdrs.v5.TableLineCompareDetailInfo`]
        """
        self._line_compare_detail_infos = line_compare_detail_infos

    @property
    def content_compare_overview_infos(self):
        """Gets the content_compare_overview_infos of this CompareResultInfo.

        内容对比概览信息体。

        :return: The content_compare_overview_infos of this CompareResultInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ContentCompareOverviewInfo`]
        """
        return self._content_compare_overview_infos

    @content_compare_overview_infos.setter
    def content_compare_overview_infos(self, content_compare_overview_infos):
        """Sets the content_compare_overview_infos of this CompareResultInfo.

        内容对比概览信息体。

        :param content_compare_overview_infos: The content_compare_overview_infos of this CompareResultInfo.
        :type content_compare_overview_infos: list[:class:`huaweicloudsdkdrs.v5.ContentCompareOverviewInfo`]
        """
        self._content_compare_overview_infos = content_compare_overview_infos

    @property
    def content_compare_detail_infos(self):
        """Gets the content_compare_detail_infos of this CompareResultInfo.

        内容对比详情信息体。

        :return: The content_compare_detail_infos of this CompareResultInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ContentCompareDetailInfo`]
        """
        return self._content_compare_detail_infos

    @content_compare_detail_infos.setter
    def content_compare_detail_infos(self, content_compare_detail_infos):
        """Sets the content_compare_detail_infos of this CompareResultInfo.

        内容对比详情信息体。

        :param content_compare_detail_infos: The content_compare_detail_infos of this CompareResultInfo.
        :type content_compare_detail_infos: list[:class:`huaweicloudsdkdrs.v5.ContentCompareDetailInfo`]
        """
        self._content_compare_detail_infos = content_compare_detail_infos

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
        if not isinstance(other, CompareResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
