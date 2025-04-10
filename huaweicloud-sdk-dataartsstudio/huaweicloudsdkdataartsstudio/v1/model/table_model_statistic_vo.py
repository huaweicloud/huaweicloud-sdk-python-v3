# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableModelStatisticVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'StatisticStandardCoverageVO',
        'published': 'StatisticStandardCoverageVO',
        'sync_total': 'SyncStatusStatisticVO',
        'physical_table': 'SyncStatusStatisticVO',
        'technical_asset': 'SyncStatusStatisticVO',
        'business_asset': 'SyncStatusStatisticVO',
        'meta_data_link': 'SyncStatusStatisticVO',
        'data_quality': 'SyncStatusStatisticVO'
    }

    attribute_map = {
        'total': 'total',
        'published': 'published',
        'sync_total': 'sync_total',
        'physical_table': 'physical_table',
        'technical_asset': 'technical_asset',
        'business_asset': 'business_asset',
        'meta_data_link': 'meta_data_link',
        'data_quality': 'data_quality'
    }

    def __init__(self, total=None, published=None, sync_total=None, physical_table=None, technical_asset=None, business_asset=None, meta_data_link=None, data_quality=None):
        r"""TableModelStatisticVO

        The model defined in huaweicloud sdk

        :param total: 
        :type total: :class:`huaweicloudsdkdataartsstudio.v1.StatisticStandardCoverageVO`
        :param published: 
        :type published: :class:`huaweicloudsdkdataartsstudio.v1.StatisticStandardCoverageVO`
        :param sync_total: 
        :type sync_total: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        :param physical_table: 
        :type physical_table: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        :param technical_asset: 
        :type technical_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        :param business_asset: 
        :type business_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        :param meta_data_link: 
        :type meta_data_link: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        :param data_quality: 
        :type data_quality: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        
        

        self._total = None
        self._published = None
        self._sync_total = None
        self._physical_table = None
        self._technical_asset = None
        self._business_asset = None
        self._meta_data_link = None
        self._data_quality = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if published is not None:
            self.published = published
        if sync_total is not None:
            self.sync_total = sync_total
        if physical_table is not None:
            self.physical_table = physical_table
        if technical_asset is not None:
            self.technical_asset = technical_asset
        if business_asset is not None:
            self.business_asset = business_asset
        if meta_data_link is not None:
            self.meta_data_link = meta_data_link
        if data_quality is not None:
            self.data_quality = data_quality

    @property
    def total(self):
        r"""Gets the total of this TableModelStatisticVO.

        :return: The total of this TableModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticStandardCoverageVO`
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this TableModelStatisticVO.

        :param total: The total of this TableModelStatisticVO.
        :type total: :class:`huaweicloudsdkdataartsstudio.v1.StatisticStandardCoverageVO`
        """
        self._total = total

    @property
    def published(self):
        r"""Gets the published of this TableModelStatisticVO.

        :return: The published of this TableModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StatisticStandardCoverageVO`
        """
        return self._published

    @published.setter
    def published(self, published):
        r"""Sets the published of this TableModelStatisticVO.

        :param published: The published of this TableModelStatisticVO.
        :type published: :class:`huaweicloudsdkdataartsstudio.v1.StatisticStandardCoverageVO`
        """
        self._published = published

    @property
    def sync_total(self):
        r"""Gets the sync_total of this TableModelStatisticVO.

        :return: The sync_total of this TableModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        return self._sync_total

    @sync_total.setter
    def sync_total(self, sync_total):
        r"""Sets the sync_total of this TableModelStatisticVO.

        :param sync_total: The sync_total of this TableModelStatisticVO.
        :type sync_total: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        self._sync_total = sync_total

    @property
    def physical_table(self):
        r"""Gets the physical_table of this TableModelStatisticVO.

        :return: The physical_table of this TableModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        return self._physical_table

    @physical_table.setter
    def physical_table(self, physical_table):
        r"""Sets the physical_table of this TableModelStatisticVO.

        :param physical_table: The physical_table of this TableModelStatisticVO.
        :type physical_table: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        self._physical_table = physical_table

    @property
    def technical_asset(self):
        r"""Gets the technical_asset of this TableModelStatisticVO.

        :return: The technical_asset of this TableModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        return self._technical_asset

    @technical_asset.setter
    def technical_asset(self, technical_asset):
        r"""Sets the technical_asset of this TableModelStatisticVO.

        :param technical_asset: The technical_asset of this TableModelStatisticVO.
        :type technical_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        self._technical_asset = technical_asset

    @property
    def business_asset(self):
        r"""Gets the business_asset of this TableModelStatisticVO.

        :return: The business_asset of this TableModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        return self._business_asset

    @business_asset.setter
    def business_asset(self, business_asset):
        r"""Sets the business_asset of this TableModelStatisticVO.

        :param business_asset: The business_asset of this TableModelStatisticVO.
        :type business_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        self._business_asset = business_asset

    @property
    def meta_data_link(self):
        r"""Gets the meta_data_link of this TableModelStatisticVO.

        :return: The meta_data_link of this TableModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        return self._meta_data_link

    @meta_data_link.setter
    def meta_data_link(self, meta_data_link):
        r"""Sets the meta_data_link of this TableModelStatisticVO.

        :param meta_data_link: The meta_data_link of this TableModelStatisticVO.
        :type meta_data_link: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        self._meta_data_link = meta_data_link

    @property
    def data_quality(self):
        r"""Gets the data_quality of this TableModelStatisticVO.

        :return: The data_quality of this TableModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        return self._data_quality

    @data_quality.setter
    def data_quality(self, data_quality):
        r"""Sets the data_quality of this TableModelStatisticVO.

        :param data_quality: The data_quality of this TableModelStatisticVO.
        :type data_quality: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusStatisticVO`
        """
        self._data_quality = data_quality

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
        if not isinstance(other, TableModelStatisticVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
