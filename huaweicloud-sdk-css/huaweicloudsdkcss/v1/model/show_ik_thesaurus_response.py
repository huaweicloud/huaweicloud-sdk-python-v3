# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIkThesaurusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'bucket': 'str',
        'main_obj': 'str',
        'stop_obj': 'str',
        'synonym_obj': 'str',
        'static_main_obj': 'str',
        'static_stop_obj': 'str',
        'extra_main_obj': 'str',
        'extra_stop_obj': 'str',
        'update_time': 'str',
        'update_details': 'str',
        'cluster_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'bucket': 'bucket',
        'main_obj': 'mainObj',
        'stop_obj': 'stopObj',
        'synonym_obj': 'synonymObj',
        'static_main_obj': 'staticMainObj',
        'static_stop_obj': 'staticStopObj',
        'extra_main_obj': 'extraMainObj',
        'extra_stop_obj': 'extraStopObj',
        'update_time': 'updateTime',
        'update_details': 'updateDetails',
        'cluster_id': 'clusterId',
        'id': 'id'
    }

    def __init__(self, status=None, bucket=None, main_obj=None, stop_obj=None, synonym_obj=None, static_main_obj=None, static_stop_obj=None, extra_main_obj=None, extra_stop_obj=None, update_time=None, update_details=None, cluster_id=None, id=None):
        r"""ShowIkThesaurusResponse

        The model defined in huaweicloud sdk

        :param status: 加载状态。  - Loaded表示加载成功。 - Loading表示正在加载中。 - Failed表示加载失败。
        :type status: str
        :param bucket: 存放词库文件的OBS桶。
        :type bucket: str
        :param main_obj: 主词库文件对象。
        :type main_obj: str
        :param stop_obj: 停词词库文件对象。
        :type stop_obj: str
        :param synonym_obj: 同义词词库文件对象。
        :type synonym_obj: str
        :param static_main_obj: 静态主词词库文件对象。
        :type static_main_obj: str
        :param static_stop_obj: 静态主词词库文件对象。
        :type static_stop_obj: str
        :param extra_main_obj: Extra主词词库库文件对象。
        :type extra_main_obj: str
        :param extra_stop_obj: Extra停词词库对象。
        :type extra_stop_obj: str
        :param update_time: 词库最近更新时间。
        :type update_time: str
        :param update_details: 更新详情。
        :type update_details: str
        :param cluster_id: 指定配置自定义词库的集群ID。
        :type cluster_id: str
        :param id: 词库的ID。
        :type id: str
        """
        
        super(ShowIkThesaurusResponse, self).__init__()

        self._status = None
        self._bucket = None
        self._main_obj = None
        self._stop_obj = None
        self._synonym_obj = None
        self._static_main_obj = None
        self._static_stop_obj = None
        self._extra_main_obj = None
        self._extra_stop_obj = None
        self._update_time = None
        self._update_details = None
        self._cluster_id = None
        self._id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if bucket is not None:
            self.bucket = bucket
        if main_obj is not None:
            self.main_obj = main_obj
        if stop_obj is not None:
            self.stop_obj = stop_obj
        if synonym_obj is not None:
            self.synonym_obj = synonym_obj
        if static_main_obj is not None:
            self.static_main_obj = static_main_obj
        if static_stop_obj is not None:
            self.static_stop_obj = static_stop_obj
        if extra_main_obj is not None:
            self.extra_main_obj = extra_main_obj
        if extra_stop_obj is not None:
            self.extra_stop_obj = extra_stop_obj
        if update_time is not None:
            self.update_time = update_time
        if update_details is not None:
            self.update_details = update_details
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if id is not None:
            self.id = id

    @property
    def status(self):
        r"""Gets the status of this ShowIkThesaurusResponse.

        加载状态。  - Loaded表示加载成功。 - Loading表示正在加载中。 - Failed表示加载失败。

        :return: The status of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowIkThesaurusResponse.

        加载状态。  - Loaded表示加载成功。 - Loading表示正在加载中。 - Failed表示加载失败。

        :param status: The status of this ShowIkThesaurusResponse.
        :type status: str
        """
        self._status = status

    @property
    def bucket(self):
        r"""Gets the bucket of this ShowIkThesaurusResponse.

        存放词库文件的OBS桶。

        :return: The bucket of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this ShowIkThesaurusResponse.

        存放词库文件的OBS桶。

        :param bucket: The bucket of this ShowIkThesaurusResponse.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def main_obj(self):
        r"""Gets the main_obj of this ShowIkThesaurusResponse.

        主词库文件对象。

        :return: The main_obj of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._main_obj

    @main_obj.setter
    def main_obj(self, main_obj):
        r"""Sets the main_obj of this ShowIkThesaurusResponse.

        主词库文件对象。

        :param main_obj: The main_obj of this ShowIkThesaurusResponse.
        :type main_obj: str
        """
        self._main_obj = main_obj

    @property
    def stop_obj(self):
        r"""Gets the stop_obj of this ShowIkThesaurusResponse.

        停词词库文件对象。

        :return: The stop_obj of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._stop_obj

    @stop_obj.setter
    def stop_obj(self, stop_obj):
        r"""Sets the stop_obj of this ShowIkThesaurusResponse.

        停词词库文件对象。

        :param stop_obj: The stop_obj of this ShowIkThesaurusResponse.
        :type stop_obj: str
        """
        self._stop_obj = stop_obj

    @property
    def synonym_obj(self):
        r"""Gets the synonym_obj of this ShowIkThesaurusResponse.

        同义词词库文件对象。

        :return: The synonym_obj of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._synonym_obj

    @synonym_obj.setter
    def synonym_obj(self, synonym_obj):
        r"""Sets the synonym_obj of this ShowIkThesaurusResponse.

        同义词词库文件对象。

        :param synonym_obj: The synonym_obj of this ShowIkThesaurusResponse.
        :type synonym_obj: str
        """
        self._synonym_obj = synonym_obj

    @property
    def static_main_obj(self):
        r"""Gets the static_main_obj of this ShowIkThesaurusResponse.

        静态主词词库文件对象。

        :return: The static_main_obj of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._static_main_obj

    @static_main_obj.setter
    def static_main_obj(self, static_main_obj):
        r"""Sets the static_main_obj of this ShowIkThesaurusResponse.

        静态主词词库文件对象。

        :param static_main_obj: The static_main_obj of this ShowIkThesaurusResponse.
        :type static_main_obj: str
        """
        self._static_main_obj = static_main_obj

    @property
    def static_stop_obj(self):
        r"""Gets the static_stop_obj of this ShowIkThesaurusResponse.

        静态主词词库文件对象。

        :return: The static_stop_obj of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._static_stop_obj

    @static_stop_obj.setter
    def static_stop_obj(self, static_stop_obj):
        r"""Sets the static_stop_obj of this ShowIkThesaurusResponse.

        静态主词词库文件对象。

        :param static_stop_obj: The static_stop_obj of this ShowIkThesaurusResponse.
        :type static_stop_obj: str
        """
        self._static_stop_obj = static_stop_obj

    @property
    def extra_main_obj(self):
        r"""Gets the extra_main_obj of this ShowIkThesaurusResponse.

        Extra主词词库库文件对象。

        :return: The extra_main_obj of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._extra_main_obj

    @extra_main_obj.setter
    def extra_main_obj(self, extra_main_obj):
        r"""Sets the extra_main_obj of this ShowIkThesaurusResponse.

        Extra主词词库库文件对象。

        :param extra_main_obj: The extra_main_obj of this ShowIkThesaurusResponse.
        :type extra_main_obj: str
        """
        self._extra_main_obj = extra_main_obj

    @property
    def extra_stop_obj(self):
        r"""Gets the extra_stop_obj of this ShowIkThesaurusResponse.

        Extra停词词库对象。

        :return: The extra_stop_obj of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._extra_stop_obj

    @extra_stop_obj.setter
    def extra_stop_obj(self, extra_stop_obj):
        r"""Sets the extra_stop_obj of this ShowIkThesaurusResponse.

        Extra停词词库对象。

        :param extra_stop_obj: The extra_stop_obj of this ShowIkThesaurusResponse.
        :type extra_stop_obj: str
        """
        self._extra_stop_obj = extra_stop_obj

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowIkThesaurusResponse.

        词库最近更新时间。

        :return: The update_time of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowIkThesaurusResponse.

        词库最近更新时间。

        :param update_time: The update_time of this ShowIkThesaurusResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def update_details(self):
        r"""Gets the update_details of this ShowIkThesaurusResponse.

        更新详情。

        :return: The update_details of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._update_details

    @update_details.setter
    def update_details(self, update_details):
        r"""Sets the update_details of this ShowIkThesaurusResponse.

        更新详情。

        :param update_details: The update_details of this ShowIkThesaurusResponse.
        :type update_details: str
        """
        self._update_details = update_details

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowIkThesaurusResponse.

        指定配置自定义词库的集群ID。

        :return: The cluster_id of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowIkThesaurusResponse.

        指定配置自定义词库的集群ID。

        :param cluster_id: The cluster_id of this ShowIkThesaurusResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def id(self):
        r"""Gets the id of this ShowIkThesaurusResponse.

        词库的ID。

        :return: The id of this ShowIkThesaurusResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowIkThesaurusResponse.

        词库的ID。

        :param id: The id of this ShowIkThesaurusResponse.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ShowIkThesaurusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
